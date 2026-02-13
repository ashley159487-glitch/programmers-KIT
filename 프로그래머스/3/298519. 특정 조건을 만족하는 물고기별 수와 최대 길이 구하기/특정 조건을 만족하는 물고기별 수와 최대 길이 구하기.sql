-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH,
FISH_TYPE FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(IFNULL(LENGTH, 10)) >= 33
ORDER BY FISH_TYPE ASC
============================================================
이 문제의 경우 HAVING절에서 그룹화된 결과에 직접 필터링을 수행하므로
서브쿼리를 쓰는 것이 아니라 HAVING절에서 필터링을 할 수 있어야 한다.

거시적인 '길' (구조 잡기)

FROM: 물고기 통을 가져온다.
WHERE: (없음) - 여기서 만약 WHERE LENGTH >= 33을 해버리면, 평균이 아니라 개별 물고기가 33미만인 애들을 다 버리게 됩니다. (그러면 평균 계산이 망가지겠죠?)
GROUP BY: 물고기 종류별로 모은다. (이때 10cm 이하는 10cm로 계산기에 입력!)
HAVING: 종류별로 계산된 평균이 33 이상인 팀만 합격시킨다.
SELECT: 합격한 팀의 마릿수(COUNT), 최대 길이(MAX), 종류를 출력한다
