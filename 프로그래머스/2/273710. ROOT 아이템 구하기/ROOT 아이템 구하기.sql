-- 코드를 작성해주세요
SELECT I.ITEM_ID, I.ITEM_NAME FROM ITEM_INFO I
JOIN ITEM_TREE T ON I.ITEM_ID = T.ITEM_ID
WHERE PARENT_ITEM_ID IS NULL
ORDER BY I.ITEM_ID ASC

이제 JOIN이 들어간 1, 2 레벨 문제는 거의 풀 수 있을 거 같다.
딱히 어려운 건 없었고, ROOT아이템은 즉 부모아이템이 NULL값일 테니까
그거만 찾는 쿼리를 만들면 된다.
