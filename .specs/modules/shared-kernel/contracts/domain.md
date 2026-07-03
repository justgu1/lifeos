# DOMAIN

## Progress

fields:

| field | type | required |
|----------|----------|----------|
| value | int (0..100) | yes |
| source_count | int (>=0) | yes |

rules:

- immutable
- value clamped to 0..100
- equality by value

## Score

fields:

| field | type | required |
|----------|----------|----------|
| points | int (>=0) | yes |
| max_points | int (>=0) | yes |
| percentage | int (0..100, derived) | yes |

rules:

- immutable
- points <= max_points
- percentage = round(points / max_points * 100) when max_points > 0 else 0
- equality by value
