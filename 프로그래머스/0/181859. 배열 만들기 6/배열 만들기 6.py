def solution(arr):
    answer = []
    for i in range(len(arr)) :
        if not answer :
            answer += [arr[i]]
        elif answer[-1] == arr[i] :
            answer = answer[:-1]
        else :
            answer += [arr[i]] 
    return answer if answer else [-1]