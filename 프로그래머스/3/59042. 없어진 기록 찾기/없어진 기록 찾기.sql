-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME FROM ANIMAL_OUTS O
LEFT JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.DATETIME IS NULL
ORDER BY O.ANIMAL_ID ASC
======================================================
입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 이런 전제조건을 가진 문제는
INNER JOIN을 쓰면 NULL값을 빼고 반환해서 정답을 맞출 수 없으므로, LEFT JOIN을 써서
기준점이 되는 컬럼은 유지시키고, 아닌쪽은 일치하는 값이 없으면 NULL을 가져오게해서
NULL값들이 있는 값들을 가져와야 한다.
