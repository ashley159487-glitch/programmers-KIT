def solution(arr, query):
    answer = []
    for i in range(len(query)) :
        if i % 2 == 0 :
            arr = arr[:query[i] + 1]
        else :
            arr = arr[query[i]:]
    for j in arr :
        answer.append(j)
    
    return answer