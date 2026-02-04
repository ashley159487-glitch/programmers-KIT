-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH,
FISH_TYPE FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(IFNULL(LENGTH, 10)) >= 33
ORDER BY FISH_TYPE ASC
============================================================
이 문제의 경우 HAVING절에서 그룹화된 결과에 직접 필터링을 수행하므로
서브쿼리를 쓰는 것이 아니라 HAVING절에서 필터링을 할 수 있어야 한다.
