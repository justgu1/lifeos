from __future__ import annotations


def _goal_event(event_id: str, expected_version: int = 0) -> dict:
    return {
        "id": event_id,
        "aggregate_id": "goal-1",
        "aggregate_type": "goal",
        "expected_version": expected_version,
        "event_type": "goal.created",
        "payload": {
            "id": "00000000-0000-0000-0000-000000000001",
            "vision_id": "00000000-0000-0000-0000-000000000002",
            "title": "Ship LifeOS",
            "created_at": "2026-07-03T12:00:00Z",
        },
    }


def test_post_events_accepts(client) -> None:
    resp = client.post("/events", json={"events": [_goal_event("EVENT0001")]})
    assert resp.status_code == 200
    body = resp.json()
    assert body["accepted"] == ["EVENT0001"]
    assert body["conflicts"] == []


def test_post_events_idempotent(client) -> None:
    payload = {"events": [_goal_event("EVENT0001")]}
    client.post("/events", json=payload)
    resp = client.post("/events", json=payload)
    assert resp.status_code == 200
    assert resp.json()["accepted"] == ["EVENT0001"]


def test_post_events_version_conflict(client) -> None:
    client.post("/events", json={"events": [_goal_event("EVENT0001", 0)]})
    resp = client.post("/events", json={"events": [_goal_event("EVENT0002", 0)]})
    assert resp.status_code == 200
    conflicts = resp.json()["conflicts"]
    assert len(conflicts) == 1
    assert conflicts[0]["reason"] == "VERSION_CONFLICT"


def test_post_events_unknown_type(client) -> None:
    event = _goal_event("EVENT0001")
    event["event_type"] = "bogus.event"
    resp = client.post("/events", json={"events": [event]})
    assert resp.status_code == 422
    assert resp.json()["detail"]["error"] == "UNKNOWN_EVENT_TYPE"


def test_post_events_invalid_payload(client) -> None:
    event = _goal_event("EVENT0001")
    del event["payload"]["title"]  # required
    resp = client.post("/events", json={"events": [event]})
    assert resp.status_code == 422
    assert resp.json()["detail"]["error"] == "VALIDATION_ERROR"
