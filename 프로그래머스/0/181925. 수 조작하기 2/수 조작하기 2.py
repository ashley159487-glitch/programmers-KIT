def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)) :
        c = numLog[i] - numLog[i-1]
        if c == 1 :
            answer += 'w'
        elif c == -1 :
            answer += 's'
        elif c == 10 :
            answer += 'd'
        elif c == -10 :
            answer += 'a'
    return answer