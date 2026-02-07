-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.NAME FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE DATEDIFF(O.DATETIME, I.DATETIME)
ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC
LIMIT 2
==================================================
나는 여태 ORDER BY는 정렬해주는 곳인줄만 알았는데
여기서도 계산이 가능했구나...
ORDER BY에서도 계산이 가능하고, 이 계산은 WHERE에서 하기 적합하지 않기 때문에
WHERE절은 지워버려야 한다.
===================================================
WHERE의 역할
  
1. 특정 값과 일치하는 데이터 (Equal)
가장 기본적으로 특정 카테고리나 이름을 찾을 때 씁니다.
WHERE NAME = 'Lucy' (이름이 루시인 동물만)
WHERE ANIMAL_TYPE = 'Dog' (개만 골라내기)
2. 범위나 크기 비교 (Comparison)
숫자나 날짜의 범위를 지정할 때 사용합니다.
WHERE DATETIME >= '2023-01-01' (2023년 이후 데이터만)
WHERE PRICE > 10000 (만원 초과 상품만)
3. 유효한 데이터만 (IS NOT NULL)
값이 비어있는(NULL) 데이터를 제외하고 싶을 때 필수입니다.
WHERE NAME IS NOT NULL (이름이 등록된 동물만)
4. 여러 조건의 조합 (AND, OR)
조건을 겹쳐서 더 정교하게 거릅니다.
WHERE ANIMAL_TYPE = 'Dog' AND INTAKE_CONDITION = 'Sick' (아픈 상태로 들어온 개만)
