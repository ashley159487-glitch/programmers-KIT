-- 코드를 작성해주세요
SELECT I.ID, N.FISH_NAME, I.LENGTH FROM FISH_INFO I
JOIN FISH_NAME_INFO N ON I.FISH_TYPE = N.FISH_TYPE
WHERE (I.FISH_TYPE, I.LENGTH) IN (SELECT FISH_TYPE, MAX(LENGTH) FROM FISH_INFO
      GROUP BY FISH_TYPE)
ORDER BY I.ID ASC
==============================================================================
메인쿼리의 WHERE절에서 여러 컬럼을 비교할 때는 반드시 () 와 IN을 써야한다.
이 문제의 경우 물고기의 종류별로 가장 큰 물고기의 ID와 이름 그리고 길이를 출력해야 하므로
메인쿼리 WHERE절에서 FISH_TYPE과 LENGTH를 서브쿼리에서 구한 값과 일치한 값만을 뽑아내
FISH_TYPE별로 그룹화 시켜준다.
