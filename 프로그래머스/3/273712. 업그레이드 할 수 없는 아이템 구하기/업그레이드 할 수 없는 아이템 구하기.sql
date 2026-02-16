-- 코드를 작성해주세요
SELECT ITEM_ID, ITEM_NAME, RARITY FROM ITEM_INFO
WHERE ITEM_ID NOT IN (SELECT PARENT_ITEM_ID FROM ITEM_TREE
                    WHERE PARENT_ITEM_ID IS NOT NULL)
ORDER BY ITEM_ID DESC
=============================================================
아직도 서브쿼리를 써야할지 조인을 써야할지 그룹화를 써야할지 해빙을 써야할지
다 헷갈린다.... 문제를 계속 푼다고 느는 것 같지가 않은데...
이번 문제의 경우 굳이 JOIN으로 합칠 필요 없이 ID가 PARENT ID 컬럼 안에
있는지 확인 하고 없으면 출력해야 하는 문제이므로 굳이 JOIN으로 합치지 않고, 
서브쿼리를 통해 컬럼 안에 없는 ID들만 출력시키면 된다.
==============================================================
SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY FROM ITEM_INFO I
LEFT JOIN ITEM_TREE T ON I.ITEM_ID = T.PARENT_ITEM_ID
WHERE T.PARENT_ITEM_ID IS NULL
ORDER BY I.ITEM_ID DESC
===============================================================
이런식으로 LEFT JOIN으로 합쳐서 나타낼 수도 있다.
