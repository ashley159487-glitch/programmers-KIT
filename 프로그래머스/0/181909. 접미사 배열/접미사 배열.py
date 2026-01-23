def solution(my_string):
    answer = []
    for i in range(len(my_string)) :
        k = my_string[i:]
        answer.append(k)
    return sorted(answer)