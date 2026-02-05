-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME ASC
LIMIT 3
======================================================
ANIMAL_OUTS의 NULL값을 구해야 하므로 LEFT JOIN을 해야한다.
IS NULL로 NULL값이 있는 값들만 추출 후 상위 셋만 출력하게 한다.
