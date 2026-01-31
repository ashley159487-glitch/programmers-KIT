-- 코드를 입력하세요
SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(*) AS PRODUCTS FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY ASC
===============================================================================
LEFT RIGHT 적어놨던 거 같은데 벌써 잊었나...
어쨌든 LEFT(PRODUCT_CODE, 2) 이렇게 쓰면 맨 왼쪽의 두 글자만 출력해준다.
그리고 GROUP BY로 나눠줘야 출력이 똑바로 된다. 안하면 하나만 이상하게 출력됨.
