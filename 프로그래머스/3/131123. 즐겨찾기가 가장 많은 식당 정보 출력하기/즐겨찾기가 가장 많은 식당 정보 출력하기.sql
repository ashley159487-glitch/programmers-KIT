-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
                                 FROM REST_INFO
                                GROUP BY FOOD_TYPE)

ORDER BY FOOD_TYPE DESC
==================================================================================
SELECT FOOD_TYPE, REST_ID, REST_NAME, MAX(FAVORITES) AS FAVORITES FROM REST_INFO
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC
이렇게 쓸 경우 FAVORITES의 최대값은 잘 갖고 오지만 그 최대값을 가진 식당의 이름은 가져오지 못하므로
서브쿼리를 이용해 FAVORITES의 최대값을 찾아낸 후 메인 쿼리에서 그 최대값에 맞는
식당이름을 매치시켜야 한다.
