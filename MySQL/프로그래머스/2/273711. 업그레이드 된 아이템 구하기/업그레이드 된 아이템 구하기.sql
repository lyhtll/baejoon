-- 코드를 작성해주세요
select i.ITEM_ID,ITEM_NAME,RARITY
from ITEM_INFO as i inner join ITEM_TREE as t 
on i.ITEM_ID = t.ITEM_ID
where PARENT_ITEM_ID in (select i.ITEM_ID
from ITEM_INFO as i,ITEM_TREE as t
where i.ITEM_ID = t.ITEM_ID and RARITY = "RARE"
)
order by i.ITEM_ID desc