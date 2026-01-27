def solution(num_list, n):
    return num_list[:n]

n번째 원소부터의 리버스 문제이다.
역시나 n + 1을 하면 틀린다.
가만 보면 문제의 제목에도 확실하게 말하고 있다.
n번째 원소 != n번째 인덱스이다.
