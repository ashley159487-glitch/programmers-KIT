-- 코드를 작성해주세요
SELECT A.ID, COUNT(B.ID) AS CHILD_COUNT FROM ECOLI_DATA A
LEFT JOIN ECOLI_DATA B ON A.ID = B.PARENT_ID
GROUP BY A.ID
ORDER BY A.ID ASC
============================================================
LEFT JOIN으로 자기 자신을 합쳐서 결과를 도출해내야 하는데 주의 할 점은
데이터끼리 매칭을 A.ID = B.PARENT_ID 이렇게 시켜야 각 ID별 그 ID를 부모로 둔 ID를 매칭 시킬수 있다.
JOIN후에 COUNT를 하면 자식이 없어 NULL인 값은 자동으로 카운트를 하지않아 0으로 출력된다.
