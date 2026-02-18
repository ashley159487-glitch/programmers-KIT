-- 코드를 입력하세요
SELECT CAR_ID, MAX(CASE WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN '대여중'
                  ELSE '대여 가능' END) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC
=========================================================================================
AVAILABILITY라는 테이블이 없으므로 CASE WHEN으로 조건을 만들어 테이블을 만들어주는데 여기서 
BETWEEN을 써줘서 START_DATE와 END_DATE의 사이에서 2022-10-16일에 대여 여부를 판별해준다.
이 CASE WHEN을 MAX로 감싸주게 되면 한 자동차의 여러 기록 중 하나라도 대여중이 있다면
그룹화 했을 때 대여중이 우선적으로 선택되게 된다.
왜 이렇게 되냐면 MAX쿼리는 문자열도 크기를 비교할 수 있기 때문이다.
컴퓨터는 문자열을 비교할 때 사전순(가나다순)으로 점수를 매긴다.
'대' (두 단어 동일)
'여' (두 단어 동일)
그다음 글자: '가' (대여 가능) vs '중' (대여중)
사전에서 '중'은 '가'보다 훨씬 뒤에 나오기 때문에 SQL은 '대여중'이 '대여 가능'보다 크다고 판단한다.
그 후 CAR_ID를 기준으로 그룹화 하면 각 CAR_ID별로 2022-10-16에 대여중인지 아닌지가 나오게 된다.
