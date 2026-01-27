SELECT * FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC

와일드 카드(%)의 위치별 의미
'네비게이션%' : 네비게이션으로 시작하는 모든 문자열
'%네비게이션' : 네비게이션으로 끝나는 모든 문자열
'%네비게이션%' : 위치에 상관 없이 네비게이션이 포함되어있는 모든 문자열
이것만 알면 풀 수 있는 문제였다.
