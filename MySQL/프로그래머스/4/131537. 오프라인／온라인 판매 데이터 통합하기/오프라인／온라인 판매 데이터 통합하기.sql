-- 코드를 입력하세요

    select date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE,PRODUCT_ID,USER_ID,SALES_AMOUNT
    from ONLINE_SALE
    where SALES_DATE like "2022-03%"
union all
    select date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE ,PRODUCT_ID,null as USER_ID,SALES_AMOUNT
    from OFFLINE_SALE
    where SALES_DATE like "2022-03%"
order by SALES_DATE asc , PRODUCT_ID asc ,USER_ID asc


# offline.sales_date,offline.product_id,offline.SALES_AMOUNT,offline.SALES_AMOUNT