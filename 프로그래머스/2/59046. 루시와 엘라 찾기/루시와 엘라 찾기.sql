-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
GROUP BY ANIMAL_ID
=========================================================================
LIKE를 쓰려면 WHERE NAME LIKE 'Lucy' OR NAME LIKE 'Ella' OR NAME LIKE 'Pickle' ...
이렇게 명령문이 엄청 길어지기 때문에 IN을 써서 한번에 조건을 맞춰야 한다.
그리고 GROUP BY같은 경우 여기서는 쓸 데가 없는 명령어이다.
GROUP BY는 보통 COUNT() 같은 집계 함수와 함께 쓸 때 사용한다.
여기서는 ORDER BY로 ANIMAL_ID기준으로 정렬해서 집계했어야 했는데
운 좋게 시스템의 기본 정렬 순서가 문제의 요구사항과 우연히 일치했기 때문에 맞춰버렸다.
너무 깊게 꼬아서 생각하지말자 생각 외로 문제는 단순한 경우가 많다.
이건 SQL이나 파이썬 기초문제나 마찬가지다.
