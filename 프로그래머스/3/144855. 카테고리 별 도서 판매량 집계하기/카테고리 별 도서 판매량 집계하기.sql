-- 코드를 입력하세요
SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES FROM BOOK B
JOIN BOOK_SALES S ON B.BOOK_ID = S.BOOK_ID
WHERE S.SALES_DATE LIKE '2022-01%'
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY ASC
===============================================================
JOIN 뒤에 따라오는 건 ON이다.
카테고리 별로 합산해야 하므로 GROUP BY 에 CATEGORY가 와야한다.
날짜를 설정 할 때 날짜는 보통 년도부터 시작하므로 '%2022-01%'이 아니라
'2022-01%'로 설정하는 게 좋다.
