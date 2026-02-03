def solution(arr):
    answer = len(arr)
    target = 1
    while target < answer :
        target *= 2
    return arr + [0] * (target - answer)