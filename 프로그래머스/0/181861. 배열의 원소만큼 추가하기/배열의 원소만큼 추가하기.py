def solution(arr):
    answer = []
    for i in arr :
        answer += [i] * i
    return answer
============================
i를 [] 로 감싸면 리스트로 만들어준다.
만약 append를 쓰려면 2중 for문을 써야한다.
