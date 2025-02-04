-- 코드를 작성해주세요
SELECT ID
FROM(
    SELECT C.ID,C.PARENT_ID
    FROM(
        SELECT A.ID,A.PARENT_ID
        FROM ECOLI_DATA as A inner join ECOLI_DATA as B
        ON A.PARENT_ID = B.ID
        ) AS C INNER JOIN 
    (
        SELECT A.ID,A.PARENT_ID
        FROM ECOLI_DATA as A inner join ECOLI_DATA as B
        ON A.PARENT_ID = B.ID
        ) AS D
    ON C.PARENT_ID = D.ID
) AS E 
where PARENT_ID not in (
    SELECT C.ID
    FROM(
        SELECT A.ID,A.PARENT_ID
        FROM ECOLI_DATA as A inner join ECOLI_DATA as B
        ON A.PARENT_ID = B.ID
        ) AS C INNER JOIN 
    (
        SELECT A.ID,A.PARENT_ID
        FROM ECOLI_DATA as A inner join ECOLI_DATA as B
        ON A.PARENT_ID = B.ID
        ) AS D
    ON C.PARENT_ID = D.ID
)
ORDER BY ID