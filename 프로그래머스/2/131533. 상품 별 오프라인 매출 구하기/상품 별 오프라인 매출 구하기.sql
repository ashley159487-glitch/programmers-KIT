-- 코드를 입력하세요
SELECT P.PRODUCT_CODE, SUM(P.PRICE * O.SALES_AMOUNT) AS SALES
FROM PRODUCT P
JOIN OFFLINE_SALE O ON P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC, P.PRODUCT_CODE ASC

어느정도 JOIN은 익숙해 진 것 같다.

각 컬럼끼리의 값을 곱하는 건 *로. 다만 SELECT바로 뒤의 *은 모든 컬럼을 뜻한다.

그리고 문제 내용에 이러한 것들이 있으면
  
~별 합계를 구해라: GROUP BY + SUM()
예: 상품별 매출 합계, 부서별 급여 합계
~별 개수를 구해라: GROUP BY + COUNT()
예: 카테고리별 상품 개수, 요일별 방문자 수
~별 평균을 구해라: GROUP BY + AVG()
예: 반별 시험 점수 평균, 월별 평균 기온
~별 최대/최소값을 구해라: GROUP BY + MAX() / MIN()
예: 제조사별 가장 비싼 상품 가격

이렇게 생각하면 된다.

그리고 HAVING에 관해서

WHERE (사전 필터링): 바구니에 담기 전에 불량품을 골라내는 것.
GROUP BY: 물건들을 종류별로 바구니에 담음.
HAVING (사후 필터링): 바구니에 다 담고 계산까지 끝난 후에, "합계가 10,000원 넘는 바구니만 가져와!"라고 바구니 자체를 검사하는 것.

이렇게 생각하자.
