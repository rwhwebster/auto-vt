WITH source AS (
    SELECT 
        COUNT(DISTINCT {{ target.source_key }})
    FROM {{ source_schema }}.{{ target.source }}
),
target AS (
    SELECT 
        COUNT(DISTINCT {{ target.primary_key }}) as total
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
    
