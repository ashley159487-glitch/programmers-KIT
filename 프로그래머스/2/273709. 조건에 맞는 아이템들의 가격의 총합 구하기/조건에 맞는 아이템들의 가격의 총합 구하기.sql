-- 코드를 작성해주세요
SELECT SUM(PRICE) AS TOTAL_PRICE FROM ITEM_INFO
WHERE RARITY = 'LEGEND'

백준허브 연동확인용 문제 풀이.

SUM관련해서는 예전에 풀어서 기억이 가물가물 했는데, 이번 문제는 간단해서 쉽게 풀렸다.
이미 테이블 안의 PRICE 컬럼의 데이터가 숫자형인 걸 알기 때문에
바로 PRICE를 SUM하면 된다.
