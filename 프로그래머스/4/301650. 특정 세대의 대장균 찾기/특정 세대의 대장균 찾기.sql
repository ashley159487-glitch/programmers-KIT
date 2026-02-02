-- 코드를 작성해주세요
SELECT ID FROM ECOLI_DATA
WHERE PARENT_ID IN (SELECT ID FROM ECOLI_DATA
                   WHERE PARENT_ID IN (SELECT ID FROM ECOLI_DATA
                                      WHERE PARENT_ID IS NULL))
ORDER BY ID ASC
==================================================================
레벨 4 치고는 쉬운 문제긴 한데 내가 처음 썼던 방식인 WHERE절에서
PARENT_ID = 3, PARENT_ID = 4 이렇게 해서 맞추는 건 틀린 방식이다.
이 문제의 요점은 내가 PARENT_ID가 뭔지 모를 때 그 값을 가져올 수 있어야 하므로,
서브쿼리를 이용해서 순차적으로 PARENT_ID가 NULL인 ID를 찾아내 그 자식ID를,
또 그 자식ID를 불러오는 방식으로 해야한다.
