-- 코드를 입력하세요
SELECT MCDP_CD AS 진료과코드, COUNT(PT_NO) AS 5월예약건수
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY COUNT(PT_NO) ASC, MCDP_CD ASC

이번 거는 문제를 따라 그대로 썼더니 바로 됐는데...
어떤 건 쉽고, 어떤 건 어렵고 SQL도 깊이가 생각보다 깊다.
그래도 이제 LIKE나 COUNT같은 명령어들을 어디서 어떻게 쓰는지 어느정도 감은 잡은 거 같아
기쁘다.
