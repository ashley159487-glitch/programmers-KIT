def solution(arr, queries):
    answer = []
    for i in range(len(arr)) :
        for j in queries :
            if j[0] <= i <= j[1] :
                arr[i] = arr[i] + 1
                
    return arr