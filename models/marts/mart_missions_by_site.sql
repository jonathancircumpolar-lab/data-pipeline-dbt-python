select
    s.site_id,
    st.parcel_status,
    count(*) as parcel_count
from {{ ref('stg_missions') }} st
left join {{ ref('sites') }} s on st.site_id = s.site_id
group by s.site_id, st.parcel_status