def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1 :
        for i in range(len(arr)) :
            if i % 2 == 0 :
                answer.append(arr[i] + n)
            else :
                answer.append(arr[i])
    elif len(arr) % 2 == 0 :
        for i in range(len(arr)) :
            if i % 2 == 1 :
                answer.append(arr[i] + n)
            else :
                answer.append(arr[i])
    return answer
=================================================
def solution(arr, n):
    answer = []
    for i, j in enumerate(arr) :
        if len(arr) % 2 == 1 and i % 2 == 0 :
            answer.append(j + n)
        elif len(arr) % 2 == 0 and i % 2 == 1 :
            answer.append(j + n)
        else :
            answer.append(j)
    return answer

이렇게 enumerate를 쓰면 더 간단해진다.
풀 때는 if조건식을 위에 넣고 그 안에 for문을 넣어서 했지만
이렇게 for문을 맨 위에 넣고 and로 각각의 조건을 합칠 수 있다.
그리고 len(arr) % 2 가 계속 반복되어 나오고 있기 때문에
변수 안에 넣고 코드를 만들면 효율성도 챙길 수 있다.
    
