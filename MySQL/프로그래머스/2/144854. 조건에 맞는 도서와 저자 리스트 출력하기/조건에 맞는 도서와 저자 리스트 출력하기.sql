-- 코드를 입력하세요
SELECT BOOK_ID,AUTHOR_NAME,date_format(PUBLISHED_DATE,'%Y-%m-%d')
from BOOK inner join AUTHOR
on BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
where category = '경제'
order by PUBLISHED_DATE asc 