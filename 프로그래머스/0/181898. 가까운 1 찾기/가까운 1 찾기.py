def solution(arr, idx):
    answer = 0
    for i in range(len(arr)) :
        if arr[i] == 1 and i >= idx :
            return i
    return -1
    