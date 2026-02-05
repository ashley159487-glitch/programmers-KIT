def solution(arr, k):
    answer = []
    for i in arr :
        if k % 2 == 1 :
            answer.append(i * k)
        else :
            answer.append(i + k)
    return answer
===================================
%연산자를 알면 쉽게 풀 수 있다.
