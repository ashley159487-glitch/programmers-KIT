def solution(num_list):
    answer = 0
    answer2 = 0
    for i in range(0, len(num_list), 2) : #홀수번째 원소들
        answer += num_list[i]
    for i in range(1, len(num_list), 2) :
        answer2 += num_list[i]
    if answer > answer2 :
        return answer
    else :
        return answer2
    
        
    