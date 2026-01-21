def solution(l, r):
    answer = []
    for i in range(l, r + 1) :
        if set(str(i)) <= {'5', '0'} : #
            answer.append(i)
    if not answer :
        answer.append(-1)
    return answer