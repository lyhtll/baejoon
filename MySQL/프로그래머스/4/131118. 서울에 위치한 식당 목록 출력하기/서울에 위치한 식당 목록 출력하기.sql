-- 코드를 입력하세요
SELECT i.REST_ID,REST_NAME,FOOD_TYPE,FAVORITES,ADDRESS,round(avg(REVIEW_SCORE),2) as SCORE
from REST_INFO as i ,REST_REVIEW as r
where i.REST_ID = r.rest_id and ADDRESS like "서울%"
group by REST_ID
order by avg(REVIEW_SCORE) desc , FAVORITES desc;