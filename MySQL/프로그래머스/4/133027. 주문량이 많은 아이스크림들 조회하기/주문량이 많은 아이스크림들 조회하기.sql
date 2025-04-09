-- 코드를 입력하세요
select FLAVOR
from (
    select sum(TOTAL_ORDER) as TOTAL_ORDER,SHIPMENT_ID
    from JULY
    group by FLAVOR
) as j inner join FIRST_HALF as f
on j.SHIPMENT_ID = f.SHIPMENT_ID
order by (f.TOTAL_ORDER + j.TOTAL_ORDER) desc
limit 3