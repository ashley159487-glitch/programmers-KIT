-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, CONCAT_WS(' ', CITY, STREET_ADDRESS1, STREET_ADDRESS2) AS '전체주소', 
CONCAT_WS('-', SUBSTR(TLNO, 1, 3), SUBSTR(TLNO, 4, 4), SUBSTR(TLNO, 8, 4)) AS '전화번호'
FROM USED_GOODS_USER U
WHERE USER_ID IN (SELECT WRITER_ID FROM USED_GOODS_BOARD
                  GROUP BY WRITER_ID HAVING COUNT(*) >= 3)
ORDER BY USER_ID DESC
==================================================================================================
CONCAT_WS는 문자열들을 합치기 전에 중간에 어떤 걸 같이 삽입 시킬지 앞에서 먼저 정하고 합쳐주는 쿼리이다.
만약 문자열들이 각각의 컬럼에 저장되어있고 각 문자열마다 띄어쓰기를 하고싶으면 먼저 ' '를 써주고 각 컬럼명을 적어주면 된다.
문자열이 하나의 컬럼 안에 들어있고 그 문자열마다 각각 중간에 글을 삽입하고 싶으면 SUBSTR을 쓰면 된다.
이번 문제는 SELECT절에서의 컬럼 합치기와 문자열 중간에 문자 삽입을 끝낼 수 있으면 비교적 쉽게 풀 수있다.
WHERE절에서 서브쿼리로 게시물을 3개 이상 쓴 WRITER_ID에 USER_ID가 있는지 확인하면 된다.
