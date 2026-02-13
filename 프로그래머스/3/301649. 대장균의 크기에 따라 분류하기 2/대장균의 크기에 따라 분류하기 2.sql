-- 코드를 작성해주세요
SELECT ID, CASE NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC)
WHEN 1 THEN 'CRITICAL'
WHEN 2 THEN 'HIGH'
WHEN 3 THEN 'MEDIUM'
WHEN 4 THEN 'LOW'
END AS COLONY_NAME FROM ECOLI_DATA
ORDER BY ID ASC
================================================================
NTILE이란?
SQL에서 데이터를 특정 개수의 그룹으로 똑같이 등분하고 싶을 때 사용하는 윈도우 함수다.
NTILE(개수) OVER (ORDER BY 기준컬럼)
NTILE은 실제 값의 차이가 아니라 데이터의 순서를 기준으로 n등분한다.
CASE WHEN으로 각각 컬럼의 이름을 따로 떼서 붙일 때 어떤 기준인지 정해준다.
