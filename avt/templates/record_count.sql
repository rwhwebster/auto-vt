WITH source AS (
    SELECT 
        {% if target.target_scd_type == 1 %}
        COUNT(DISTINCT {{ target.source_key }})
        {% else %}
        COUNT(1) as total
        {% endif %}
    FROM {{ source_schema }}.{{ target.source }}
),
target AS (
    SELECT COUNT(1) as total
    FROM {{ target_schema }}.{{ target.name }}
)
SELECT
    source.total AS SOURCE_COUNT,
    target.total AS TARGET_COUNT,
    (target.total - source.total) AS COUNT_DIFF
FROM source
FULL OUTER JOIN target
    
