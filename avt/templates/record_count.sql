WITH source AS (
    SELECT COUNT(1) as total
    FROM {{ source_schema }}.{{ source_table }}
),
target AS (
    SELECT COUNT(1) as total
    FROM {{ target_schema }}.{{ target_table }}
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
    
