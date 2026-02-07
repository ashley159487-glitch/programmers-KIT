-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/', F.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD B JOIN USED_GOODS_FILE F ON B.BOARD_ID = F.BOARD_ID
WHERE B.BOARD_ID = (SELECT BOARD_ID FROM USED_GOODS_BOARD ORDER BY VIEWS DESC LIMIT 1)
ORDER BY F.FILE_ID DESC
=======================================================================================================
기존 테이블에 없는 새로운 컬럼을 만들라고 하는 문제는 언제나 당황스럽다.
이 문제는 거기에다가 그 컬럼 내용을 직접 이어 붙여야하는 문제여서 처음엔 더 하기 싫었지만
그거만 이어 붙이면 나머지 쿼리는 그나마 간단해서 꽤 쉽게 풀 수 있었다.
위의 쿼리는 서브쿼리 안에 ORDER BY로 VIEWS를 DESC 한 후 가장 위에만 잘라서 비교했지만
SELECT절에서 바로 MAX로 가장 높은 거만 골라내서 비교해도 된다.
======================================================================================================
SELECT CONCAT('/home/grep/src/', F.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD B JOIN USED_GOODS_FILE F ON B.BOARD_ID = F.BOARD_ID
WHERE B.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY F.FILE_ID DESC
