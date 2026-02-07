def solution(array, commands):
    answer = []
    for i, j, k in commands :
        a = sorted(array[i - 1:j])
        answer.append(a[k - 1])
    return answer
=====================================
2차원배열은 반복문에 언패킹으로 각각 값에 들어있는 값들을
빼낼 수 있다. 그 후에는 문제에서 요구한 것 처럼 코드를 짜면 된다.
주의할 점은 인덱스를 세는 법과 그냥 세는 법이 다르므로
array의 i번째부터는 i-1로 만들어줘야한다.
