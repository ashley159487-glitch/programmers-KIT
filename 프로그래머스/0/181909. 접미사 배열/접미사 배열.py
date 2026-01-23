def solution(my_string):
    answer = []
    for i in range(len(my_string)) :
        k = my_string[i:]
        answer.append(k)
    return sorted(answer)

정렬은 sort를 써야한다. 잊으면 안된다 이제.
