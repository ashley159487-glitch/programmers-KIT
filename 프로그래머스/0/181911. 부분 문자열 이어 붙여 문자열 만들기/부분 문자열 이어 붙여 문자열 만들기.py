def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)) :
        q = my_strings[i]
        k = q[parts[i][0]:parts[i][1] + 1]
        answer += k
    return answer
       