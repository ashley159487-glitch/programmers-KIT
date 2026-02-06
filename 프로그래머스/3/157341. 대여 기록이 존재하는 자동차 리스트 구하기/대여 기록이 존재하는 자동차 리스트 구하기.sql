-- 코드를 입력하세요
SELECT DISTINCT C.CAR_ID FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY R ON C.CAR_ID = R.CAR_ID
WHERE C.CAR_TYPE = '세단' AND MONTH(R.START_DATE) = 10
ORDER BY C.CAR_ID DESC
================================================================
아직 서브쿼리랑 조인을 어느 상황에 써야하는지 감은 잘 안잡히지만
그래도 문제를 보면 머릿속에서 조인을 이렇게 하고 서브쿼리를 이렇게 넣으면
추출 가능 할 거 같은데? 라는 생각은 든다. 조금만 더 해보면 될 듯 싶다.

DISTINCT는 "중복된 값을 제거하고 고유한 값만 보여달라"고 명령하는 키워드이다.
문제에 중복이 없어야 한다고 하기 때문에 DISTINCT를 써주거나 GROUP BY로 중복을 없애주면 된다.
