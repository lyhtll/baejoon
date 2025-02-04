-- 코드를 작성해주세요
select ID, COLONY_NAME
from (
    select *,
        case ntile(4) over (ORDER BY SIZE_OF_COLONY)
            when 4 then 'CRITICAL'
            when 3 then 'HIGH'
            when 2 then 'MEDIUM'
            when 1 then 'LOW'
        END AS COLONY_NAME
    from ECOLI_DATA
) AS A
ORDER BY ID
