with source as (
    select *
    from {{ source('northwind', 'customer') }}
)

select
    *,
    current_localtime() as ingestion_timestamp
from source