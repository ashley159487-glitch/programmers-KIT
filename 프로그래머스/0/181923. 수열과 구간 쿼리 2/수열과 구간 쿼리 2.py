def solution(arr, queries):
    answer = []
    for s, e, k in queries :
        c = []
        for i in range(s, e + 1) :
            if arr[i] > k :
                c.append(arr[i])
        if c :
            answer.append(min(c))
        else :
            answer.append(-1)
            
    return answer