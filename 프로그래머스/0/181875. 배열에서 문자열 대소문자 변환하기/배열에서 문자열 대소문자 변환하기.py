def solution(strArr):
    answer = []
    for i, j in enumerate(strArr) :
        if i % 2 == 0 :
            j = j.lower()
            answer.append(j)
        else :
            j = j.upper()
            answer.append(j)
    return answer