with source as (
    select *
    from {{ source('northwind', 'products') }}
    where supplier_ids not like '%;%'
)

select
    *,
    current_localtime() as ingestion_timestamp
from source