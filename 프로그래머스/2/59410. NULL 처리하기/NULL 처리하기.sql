-- 코드를 입력하세요
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC

IFNULL의 각 절에서 사용 상황
1. ORDER BY 절에서 사용 (정렬할 때)
NULL 값을 가진 데이터를 가장 아래로 보내거나 특정 순서에 맞추고 싶을 때 사용합니다.
예시: ORDER BY IFNULL(SCORE, 0) DESC
의미: 점수가 NULL인 사람을 0점으로 간주하고 내림차순 정렬해라.
2. WHERE 절에서 사용 (조건 필터링할 때)
NULL 데이터까지 포함해서 조건을 걸고 싶을 때 유용합니다.
예시: WHERE IFNULL(FISH_NAME, '미등록') = '미등록'
의미: 이름이 NULL이거나 '미등록'인 데이터를 모두 찾아라.
3. GROUP BY 절에서 사용 (그룹 묶을 때)
NULL 값들을 별도의 그룹이 아닌 특정 명칭으로 합쳐서 묶고 싶을 때 씁니다.
예시: GROUP BY IFNULL(TYPE, '기타')
의미: TYPE이 없는 데이터들을 모두 '기타'라는 그룹 하나로 묶어서 통계를 내라.
4. 왜 SELECT에서 제일 많이 보이나요?
주로 사용자에게 결과를 보여줄 때 "빈칸(NULL)" 대신 "없음"이나 "0"으로 예쁘게 바꿔서 보여줘야 하기 때문에 SELECT 절에서 가장 자주 쓰이는 것뿐입니다.
