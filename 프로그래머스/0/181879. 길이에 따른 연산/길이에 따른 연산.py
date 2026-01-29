def solution(num_list):
    answer = 0
    if len(num_list) >= 11 :
        for i in num_list :
            answer += i
    else :
        answer = 1
        for i in num_list :
            answer *= i
    return answer
================================
for문 안에서 변수를 재선언 하면 반복이 돌 때마다 변수값이 계속
재선언되기 때문에 변수의 재선언은 반복문 밖에다 하는 것이 좋다.
