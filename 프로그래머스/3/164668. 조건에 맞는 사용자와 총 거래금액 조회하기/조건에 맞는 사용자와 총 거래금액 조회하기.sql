-- 코드를 입력하세요
SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID
WHERE STATUS = 'DONE'
GROUP BY U.USER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES ASC
====================================================================================
문제를 보고 구조를 먼저 짜는 연습을 해야겠다.
구조를 먼저 짜니까 어떻게 명령문을 적어야 할 지가 머릿속에 그려지고, 쉽게 풀 수 있었다.
