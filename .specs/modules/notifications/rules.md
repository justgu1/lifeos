# RULES

## REQUIRED

- RULE-001: notification hours come from Config.notification_hours (default [13,18,22])
- RULE-002: honor timezone and quiet hours from Config
- RULE-003: never notify when there are zero pending blocks
- RULE-004: reminders open the check-in directly

## SECURITY

- no PII in notification payload logs

## PERFORMANCE

- batch-schedule reminders once per day

## OBSERVABILITY

- expose delivery success and skip metrics

## EXCEPTIONS

| rule | exception |
|----------|----------|
