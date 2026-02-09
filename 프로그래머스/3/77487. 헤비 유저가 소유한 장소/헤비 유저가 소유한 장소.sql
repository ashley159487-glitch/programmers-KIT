-- 코드를 입력하세요
SELECT * FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID FROM PLACES
                GROUP BY HOST_ID
                HAVING COUNT(*) >= 2)
ORDER BY ID ASC
===============================================
메인 쿼리에서 GROUP BY와 HAVING으로 조건을 잡으면 결과물이
HOST_ID별 하나씩만 뜨기때문에 서브쿼리를 이용해 전제 결과물이 나오게 보여준다.
