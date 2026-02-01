-- 코드를 작성해주세요
SELECT YEAR(YM) AS YEAR, ROUND(AVG(PM_VAL1), 2) AS 'PM10', 
ROUND(AVG(PM_VAL2), 2) AS 'PM2.5'
FROM AIR_POLLUTION
WHERE LOCATION1 LIKE '%경기%' AND LOCATION2 LIKE '%수원%'
GROUP BY YEAR
ORDER BY YEAR ASC
============================================================

=의 경우 완벽하게 똑같은 값을 찾을 때 이용하고
LIKE의 경우 찾고싶은 글자가 포함되어있나를 확인 할 때 사용한다.
