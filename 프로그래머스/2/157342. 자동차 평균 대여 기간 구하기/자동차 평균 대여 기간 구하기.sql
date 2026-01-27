SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC

날짜간의 차를 구할 때는 DATEDIFF를 쓰고 + 1을 해야한다.
왜냐하면 빌린 당일부터 세야하는데 + 1을 안하면 빌린 당일을 빼버리기 때문이다.
그렇게 평균을 구했으면 CAR_ID를 그룹별로 나눠야 한다.
GROUP BY를 안하니까 쿼리가 한 줄만 출력이 됐다.
CAR_ID별로 출력을 해야하니까 GROUP BY를 하고
HAVING으로 빌린 날짜가 7일 이상인 것들만 추려내야 한다.
WHERE과 HAVING의 차이는
WHERE는 데이터를 가져올 때 바로 검사하는 조건이고,
HAVING은 그룹화하여 계산(AVG)이 끝난 결과값에 조건을 거는 것이다. "평균을 내보니 7일 이상이더라!"는 집계 이후의 일이라 HAVING을 쓴다.
