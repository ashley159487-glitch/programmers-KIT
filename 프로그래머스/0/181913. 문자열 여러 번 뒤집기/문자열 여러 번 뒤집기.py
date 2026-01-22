def solution(my_string, queries):
    answer = ''
    c = list(my_string)
    for s, e in queries :
        c[s:e + 1] = c[s:e + 1][::-1]
    return answer.join(c)