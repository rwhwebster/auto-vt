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
    'Source Record Count:' AS label,
    total
FROM source

UNION ALL

SELECT 
    'Target Record Count:' as label,
    total
FROM target
    
