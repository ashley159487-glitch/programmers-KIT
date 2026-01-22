def solution(my_string, queries):
    answer = ''
    c = list(my_string)
    for s, e in queries :
        c[s:e + 1] = c[s:e + 1][::-1]
    return answer.join(c)

슬라이싱을 많이 써본적이 없어서 이번 문제를 봤을 때
각 인덱스의 위치를 바꾸려고만 했다..
뒤집어라 = [::-1] 기억하자.
어느 구간을 변경하거나 하는 문제는 슬라이싱을 쓴다.
