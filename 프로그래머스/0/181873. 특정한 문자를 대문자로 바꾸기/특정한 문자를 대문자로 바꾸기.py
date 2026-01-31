def solution(my_string, alp):
    answer = ''
    for i in my_string :
        if i == alp :
            answer += i.upper()
        else :
            answer += i
    return answer
=================================
문제 그대로 코드로 쉽게 옮길 수 있는 문제였다.
