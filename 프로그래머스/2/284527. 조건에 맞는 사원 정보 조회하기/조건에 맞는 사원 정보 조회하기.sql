-- 코드를 작성해주세요
SELECT SUM(G.SCORE) AS SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES E JOIN HR_GRADE G ON E.EMP_NO = G.EMP_NO
WHERE G.YEAR = 2022
GROUP BY E.EMP_NO
ORDER BY SCORE DESC
LIMIT 1

컬럼이 3개 있길래 이거 2레벨 맞아? 했는데 하나는 무시해도 됐었다.
두 개의 컬럼만 사용하면 되므로 JOIN으로 쓰는 두 컬럼을 묶고,
모두와 다르게 식별 할 수 있는 EMP_NO로 GROUP BY한다.
가장 높은 점수가 나와야 하므로 DESC를 하고 LIMIT으로 가장 높은 점수
한 명만 보이게 한다.
