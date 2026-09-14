select
    mission_id,
    agent_id,
    site_id,
    cast(mission_date as date) as mission_date,
    coalesce(parcel_status, 'Unknown') as parcel_status,
    validation_delay_days
from {{ ref('missions') }}