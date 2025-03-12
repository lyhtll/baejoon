-- 코드를 작성해주세요
select ITEM_ID,ITEM_NAME,RARITY
from ITEM_INFO
where ITEM_ID not in(select i.ITEM_ID
from ITEM_INFO as i ,ITEM_TREE as t
where i.ITEM_ID = PARENT_ITEM_ID)
order by ITEM_ID desc
