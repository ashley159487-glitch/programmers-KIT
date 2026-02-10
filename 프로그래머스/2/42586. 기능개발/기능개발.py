def solution(progresses, speeds):
    answer = []
    for i, j in enumerate(progresses) :
        days = (100 - j + speeds[i] - 1) // speeds[i]
        answer.append(days)
    target = answer[0]
    cnt = 1
    last = []
    for i in range(1, len(answer)) :
        if target >= answer[i] :
            cnt += 1
        else :
            last.append(cnt)
            cnt = 1
            target = answer[i]
    last.append(cnt)
    return last