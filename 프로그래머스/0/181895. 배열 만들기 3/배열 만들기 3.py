def solution(arr, intervals):
    answer = []
    for i in intervals :
        a, b = i
        for j in range(a, b + 1) :
            answer.append(arr[j])
            
    return answer