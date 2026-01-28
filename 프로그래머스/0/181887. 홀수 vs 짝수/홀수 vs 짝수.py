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
==============================================================
처음에
def solution(num_list):
    answer = 0
    answer2 = 0
    for i in range(len(num_list)) :
        if i % 2 == 0 :
            answer += num_list[i]
        else :
            answer2 += num_list[i]
            return max(answer, answer2)
이렇게 만들고 테스트를 시도해보는데 계속 테스트가 실패하길래
그냥 아예 처음부터 끝까지 다 써보자 하는 마음으로 각각 for문을 돌리다가
return이 for문 안에 있어서 답이 틀리는 것이었다는 걸 알았다.
그냥 계속 쭉 코드를 써서 for문이 2개 있는 코드로 답을 맞추긴 했는데
들여쓰기가 어디에 어떻게 되어있는지 꼭 유념하면서 문제를 풀어야겠다.
    
        
    
