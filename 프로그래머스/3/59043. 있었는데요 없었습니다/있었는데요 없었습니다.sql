-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME FROM ANIMAL_OUTS O
JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE O.DATETIME < I.DATETIME
ORDER BY I.DATETIME ASC
==================================================
두 테이블 안에 같은 컬럼이 있다고 아무거나 막 묶어서 JOIN하면 데이터가 엉망으로 나온다.
FK가 될만한 컬럼을 찾아 JOIN하는 것이 중요하다.
