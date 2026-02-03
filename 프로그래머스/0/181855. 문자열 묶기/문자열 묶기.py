def solution(strArr):
    answer = []
    cnt = []
    for i in strArr :
        answer.append(len(i))
    for j in set(answer) :
        cnt.append(answer.count(j))
    return max(cnt)