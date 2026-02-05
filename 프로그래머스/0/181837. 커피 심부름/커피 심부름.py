def solution(order):
    answer = 0
    for i in order :
        if "latte" in i :
            answer += 5000
        else :
            answer += 4500
    return answer
=============================
라떼가 들어있는 문자열만 먼저 5000으로 처리하면
나머지(아메리카노, anything)은 else하나로 처리가 가능하다.
조건문의 우선순위를 활용한 전략을 잘 생각하자.
