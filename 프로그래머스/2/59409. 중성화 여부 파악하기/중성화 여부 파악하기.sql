-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, CASE
WHEN SEX_UPON_INTAKE LIKE '%Neutered%'
OR SEX_UPON_INTAKE LIKE "%Spayed%"
THEN 'O'
ELSE 'X'
END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC
=======================================
처음엔 쉬워보였던 SQL쿼리가 파이썬보다 더 어려워진 느낌이다.
일단 명령문 자체의 응용을 못하기도 하고, 알고 있는 명령문 자체도
그 수가 별로 없어서도 그렇고 설사 알고있는 명령문이라 할지라도
그의 응용을 배운적이 없고, 단지 알고만 있는 거라 응용이 힘들기도 하다.
위의 문제같은 경우 중성화 여부를 체크하고, 되있으면 테이블 안의 내용을
O, X로 바꿔주는 것이기 때문에 CASE WHEN으로 조건들을 체크하고
THEN ELSE로 여부를 나눠준 후 컬럼명도 바꿔줘야 한다.
