def solution(arr, delete_list):
    answer = []
    for i, j in enumerate(arr) :
        if j not in delete_list :
            answer.append(j)
    
    return answer