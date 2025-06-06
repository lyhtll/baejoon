-- 코드를 입력하세요
SELECT TITLE,b.BOARD_ID,REPLY_ID,r.WRITER_ID,r.CONTENTS,left(r.CREATED_DATE,10)
from USED_GOODS_BOARD as b,USED_GOODS_REPLY as r
where r.BOARD_ID = b.BOARD_ID and b.CREATED_DATE like "2022-10%"
order by r.CREATED_DATE asc, TITLE asc;