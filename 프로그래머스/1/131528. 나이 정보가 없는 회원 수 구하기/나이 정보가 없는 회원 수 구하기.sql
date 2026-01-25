-- 코드를 입력하세요
SELECT COUNT(*) AS USERS FROM USER_INFO
WHERE AGE IS NULL

IS NULL 은 확인 할 때 IFNULL은 바꿀 때 쓴다.
이 문제는 단순한 확인 이므로 IS NULL 을 쓴다.
