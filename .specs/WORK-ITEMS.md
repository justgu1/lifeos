# WORK ITEMS

| id | module | status | priority | depends_on |
|----------|----------|----------|----------|----------|
| TEMPLATE-001 | template | draft | high | [] |
| PLATFORM-001 | platform | active | high | [] |
| SHARED-001 | shared-kernel | active | high | [PLATFORM-001] |
| PLATFORM-002 | platform | active | high | [PLATFORM-001, SHARED-001] |
| STRATEGY-001 | strategy | draft | high | [PLATFORM-002, SHARED-001] |
| ROUTINE-001 | routine | draft | high | [STRATEGY-001] |
| PLANNING-001 | planning | draft | high | [ROUTINE-001] |
| SETUP-001 | setup | draft | high | [PLANNING-001] |
| CHECKIN-001 | check-in | draft | high | [PLANNING-001] |
| CHECKIN-002 | check-in | draft | high | [CHECKIN-001] |
| REVIEW-001 | review | draft | medium | [CHECKIN-001] |
| REVIEW-002 | review | draft | medium | [REVIEW-001, PLANNING-001] |
| REVIEW-003 | review | draft | medium | [REVIEW-002] |
| PLATFORM-003 | platform | draft | medium | [PLATFORM-002, CHECKIN-001] |
| PLATFORM-004 | platform | draft | medium | [CHECKIN-002] |
| NOTIF-001 | notifications | draft | medium | [CHECKIN-001] |
| COACH-001 | ai-coach | draft | low | [REVIEW-002, PLATFORM-003] |
