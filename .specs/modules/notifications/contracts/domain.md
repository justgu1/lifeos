# DOMAIN

## Notification

Value object.

fields:

| field | type | required |
|----------|----------|----------|
| id | uuid | yes |
| type | enum(midday,evening,night) | yes |
| scheduled_for | timestamp | yes |
| payload | json | yes |
| status | enum(scheduled,sent,skipped) | yes |

rules:

- hours come from Config.notification_hours
- skip when zero pending blocks
- honor timezone and quiet hours
- payload carries e.g. pending_count and message
