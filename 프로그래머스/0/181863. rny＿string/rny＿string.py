def solution(rny_string):
    answer = ''
    for i in rny_string :
        if i == "m" :
            answer += "rn"
        else :
            answer += i
    return answer
=============================
이런 문제를 풀 때는 치환하는 값 말고 그대로 들어가야 하는 값들도 생각을 해줘야 한다.
치환만 하면 치환한 값들만 들어가므로 오답이기 때문에 else로 기존 값들은 그대로 넣어줘야 한다.
