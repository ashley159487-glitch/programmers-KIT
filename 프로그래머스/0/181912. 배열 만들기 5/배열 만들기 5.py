def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs :
        sli = int(i[s:s + l])
        if sli > k :
            answer.append(sli)
    return answer