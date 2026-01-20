-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기%'
ORDER BY WAREHOUSE_ID ASC

SQL 분명 1레벨들만 풀 때는 쉬워보였는데 세상에 쉬운 건 하나도 없나보다...
IFNULL(컬럼명, '대체할값')은 이 컬럼이 비어있으면 대체할 값으로 채워달라는 뜻.
IFNULL만 알아도 바로 풀 수 있는 문제.
WHERE은 데이터를 필터링 할 때만 쓰기 때문에 무언가 데이터를 가공 해야할 일이 생기면
SELECT에서 해야한다.
