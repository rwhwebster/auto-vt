SELECT {{ target.primary_key }}, COUNT(1)
FROM {{ target_schema }}.{{ target.name }}
GROUP BY {{ target.primary_key }}
HAVING COUNT(1) > 1
