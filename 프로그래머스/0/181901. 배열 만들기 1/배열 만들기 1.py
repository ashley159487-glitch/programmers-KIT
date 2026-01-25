def solution(n, k):
    answer = []
    for i in range(k, n + 1, k) :
        answer.append(i)
    return answer

range(k, n, k)로 할 경우
n이 k의 배수에 포함되면 n은 출력이 안되기 때문에 오답이 됨.
