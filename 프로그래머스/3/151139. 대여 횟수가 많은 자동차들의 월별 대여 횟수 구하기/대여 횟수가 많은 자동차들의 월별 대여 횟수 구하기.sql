-- 코드를 입력하세요
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
                GROUP BY CAR_ID
                HAVING COUNT(*) >= 5)
AND START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY MONTH, CAR_ID
HAVING RECORDS > 0
ORDER BY MONTH ASC, CAR_ID DESC
==========================================================================
이 문제는 아직 내 것이 아니므로 상세히 기록해야겠다.
대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 => 대여시작일로 명시되어 있으므로 START_DATE로만 MONTH로 만든다.
총 대여 횟수가 5회 이상인 자동차들에 대해서 해당 기간 동안의 월별 자동차 ID => CAR_ID 를 써야하는 이유.
ID 별 총 대여 횟수(컬럼명: RECORDS) => 이 거 까지해서 총 3가지를 컬럼에 나타내야한다.
CAR_ID 별 총 대여 횟수이므로 WHERE절에서 CAR_ID 기준으로 서브쿼리를 만드는데, 
2022년 8월~10월 사이에 총 대여 횟수가 5회 이상인 자동차 ID를 이 서브쿼리에서 뽑는 것.
서브쿼리에서 자동차 ID를 뽑았으면 착각하기 쉬운게 서브쿼리에서 날짜를 필터링 한 것이 아니라
그 기간 안에 5회 이상 빌려간 자동차 ID만 나오므로 메인 쿼리의 WHERE에서 날짜를 필터링 해줘야한다.
그리고 월 별 자동차 ID 별 총 대여 횟수이므로 GROUP BY에 MONTH랑 CAR_ID를 둘다 넣어줘야 한다.
