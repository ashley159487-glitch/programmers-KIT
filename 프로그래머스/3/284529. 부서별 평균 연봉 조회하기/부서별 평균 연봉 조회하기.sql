-- 코드를 작성해주세요
SELECT D.DEPT_ID, D.DEPT_NAME_EN, ROUND(AVG(E.SAL)) AS AVG_SAL
FROM HR_DEPARTMENT D JOIN HR_EMPLOYEES E ON D.DEPT_ID = E.DEPT_ID
GROUP BY D.DEPT_ID
ORDER BY AVG_SAL DESC
===================================================================
이 문제에서 SAL은 사원별 연봉이지만 GROUP BY에서 부서별로 묶는 순간
DEPT_ID가 같은 사원들을 하나로 묶고 그 묶은 사원들의 평균 연봉을 계산해준다.
