def solution(str_list, ex):
    answer = ''
    for i in str_list :
        if ex not in i :
            answer += i
    return answer
=============================
리스트 형식이므로 반복문으로 각 문자열을 빼내어
ex가 있는 문자열 빼고 나머지를 문자열로 합치면 된다.
