def solution(names):
    answer = names[::5]
    
    return answer
=============================
어이가 없을 정도로 쉬운 문제지만
며칠 전의 나였으면 이걸
def solution(names):
    answer = []
    for i in range(0, len(names), 5) :
        answer.append(names[i])
    return answer
이런 식으로 for문을 써서 풀었을 거 같다.
슬라이싱의 편리함이 다시끔 remind되는 문제였다.
