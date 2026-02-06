def solution(arr):
    answer = []
    for i in arr :
        while len(arr) > len(i) :
            i.append(0)
        answer.append(i)    
    while len(answer[0]) > len(answer) :
        answer.append([0] * len(answer[0]))                
    return answer