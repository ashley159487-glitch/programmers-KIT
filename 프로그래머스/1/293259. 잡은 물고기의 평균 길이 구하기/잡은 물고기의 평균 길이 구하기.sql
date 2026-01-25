-- 코드를 작성해주세요
SELECT ROUND(AVG(IFNULL(LENGTH, 10)), 2) AS AVERAGE_LENGTH FROM FISH_INFO

괄호가 여려개 겹쳐서 들어가니까 가독성이 떨어진다.
쳐져있는 괄호에 맞게 각 쿼리를 집어 넣자.
