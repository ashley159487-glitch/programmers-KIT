def solution(arr, queries):
    answer = []
    for i, j in queries :
        arr[i], arr[j] = arr[j], arr[i]
        
    return arr