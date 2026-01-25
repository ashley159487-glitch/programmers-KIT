-- 코드를 작성해주세요
SELECT ROUTE, CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE,
CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY SUM(D_BETWEEN_DIST) DESC

문제가 까다롭고 어렵다기 보다는 복잡해서 집중력을 흐트려놓는다...

COCAT은 앞 뒤 이어붙이기
ROUND는 숫자를 반올림 하기
다 했던 것들인데 활용 할 수 조차 없었다...
일단 힘들어도 문제를 천천히 뜯어볼 수 있어야 할 거 같다.
