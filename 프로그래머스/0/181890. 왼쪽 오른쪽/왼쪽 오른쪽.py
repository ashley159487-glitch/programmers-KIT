def solution(str_list):
    answer = []
    for i, char in enumerate(str_list) :
        if char == 'l' :
            return str_list[:i]
        elif char == 'r' :
            return str_list[i+1:]
    return answer

이런 식의 인덱스 문제는 사람이 인지하는 수의 증가와 인덱스의 증가의 괴리감을 지우는 수련을 하는 것 같다.

코딩 자체는 별로 어려운 건 없었다. 문제 그대로 코드를 치니 답이 나왔다.
며칠 전의 나였으면 많이 고민하다가 결국 제미나이한테 물어봤을 문제였다.

enumerate를 가장 적절하게 쓸 수 있는 문제라고 생각한다. 처음엔 range(len())으로 풀까 했으나
그것보다는 enumerate가 더 깔끔하게 생각하는 대로 쓸 수 있어서 enumerate를 사용했다.
            
    
