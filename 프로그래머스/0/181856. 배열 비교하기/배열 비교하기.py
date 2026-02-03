def solution(arr1, arr2):
    answer = 0
    answer1 = 0
    if len(arr1) < len(arr2) :
        return -1
    if len(arr1) > len(arr2) :
        return 1
    if len(arr1) == len(arr2) :
        for i in arr1 :
            answer += i
        for j in arr2 :
            answer1 += j
    if answer == answer1 :
        return 0
    if answer > answer1 :
        return 1
    else :
        return -1
    
    