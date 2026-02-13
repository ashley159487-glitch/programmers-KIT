-- 코드를 작성해주세요
SELECT ID, CASE
WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
WHEN SIZE_OF_COLONY <= 1000 THEN 'MEDIUM'
ELSE 'HIGH'
END AS SIZE
FROM ECOLI_DATA
ORDER BY ID ASC
=============================================
CASE WHEN에 익숙해져야 한다.
CASE WHEN이란?
컬럼 내에서 각각의 값을 원래의 결과물 말고 내가 원하는 기준에 맞춰서 새로운 값으로 바꿔주는 쿼리이다.
