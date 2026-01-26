def solution(arr):
    answer = []
    indexes = []
    for i in range(len(arr)) :
        if arr[i] == 2 :
            indexes.append(i)
    if len(indexes) == 0 :
        return [-1]
    start = indexes[0]
    end = indexes[-1]
    answer = arr[start:end + 1]
            
            
    return answer