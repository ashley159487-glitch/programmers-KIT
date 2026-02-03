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
===================================
sum() 함수를 사용하면 훨씬 쉽게 풀 수 있다.

def solution(arr1, arr2):
    if len(arr1) > len(arr2) :
        return 1
    elif len(arr1) < len(arr2) :
        return -1

    sum1 = sum(arr1)
    sum2 = sum(arr2)
    
    if sum1 > sum2 :
        return 1
    elif sum1 < sum2 :
        return -1
    else :
        return 0
    
    
