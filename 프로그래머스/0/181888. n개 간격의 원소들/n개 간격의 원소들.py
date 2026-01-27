def solution(num_list, n):
    return num_list[::n]

이번의 정수 n은 간격으로 사용해야 하므로
[::n]을 할 경우
가장 처음 값부터 마지막 값까지 n번째만 뽑아내라 라는 뜻이 된다.
