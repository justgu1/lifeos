"""POST /events — the single write path (platform)."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.application.commands.append_events import AppendEventsCommand, IncomingEvent
from app.infrastructure.db.session import get_session
from app.infrastructure.event_store import UnknownEventTypeError

router = APIRouter(tags=["events"])


class EventIn(BaseModel):
    id: str
    aggregate_id: str
    aggregate_type: str
    expected_version: int = Field(ge=0)
    event_type: str
    schema_version: int = 1
    payload: dict
    created_at: str | None = None


class AppendRequest(BaseModel):
    events: list[EventIn]


class ConflictOut(BaseModel):
    id: str
    reason: str
    expected: int | None = None
    actual: int | None = None


class AppendResponse(BaseModel):
    accepted: list[str]
    conflicts: list[ConflictOut]


@router.post("/events", response_model=AppendResponse)
def append_events(
    request: AppendRequest, session: Session = Depends(get_session)
) -> AppendResponse:
    command = AppendEventsCommand()
    incoming = [
        IncomingEvent(
            id=e.id,
            aggregate_id=e.aggregate_id,
            aggregate_type=e.aggregate_type,
            expected_version=e.expected_version,
            event_type=e.event_type,
            payload=e.payload,
            schema_version=e.schema_version,
            created_at=e.created_at,
        )
        for e in request.events
    ]
    try:
        result = command.execute(session, incoming)
    except UnknownEventTypeError as exc:
        raise HTTPException(
            status_code=422,
            detail={"error": "UNKNOWN_EVENT_TYPE", "event_type": exc.event_type},
        ) from exc
    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail={"error": "VALIDATION_ERROR", "message": str(exc)},
        ) from exc

    return AppendResponse(
        accepted=result.accepted,
        conflicts=[ConflictOut(**c) for c in result.conflicts],
    )
