-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE LIKE 'DOG'
ORDER BY NAME ASC
===================================================
WHERE절에서 한 번에 두가지의 조건을 걸 수 있다.
그리고 찾으려고 하는 값이 딱 하나로 떨어지는 조건이면
LIKE대신 =를 쓸 수 있다.
