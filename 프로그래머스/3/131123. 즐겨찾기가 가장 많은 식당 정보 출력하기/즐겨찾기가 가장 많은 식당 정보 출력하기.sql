-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES) FROM REST_INFO
                                GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC
====================================================================================
즐겨찾기수가 가장 많은 식당의 음식 종류
문제에서 이거만 보고 식당 이름을 썼는데 종류로 구분해야 하기 때문에 음식 종류로 서브쿼리를 만들어야한다.
