def solution(arr, query):
    answer = []
    for i in range(len(query)) :
        if i % 2 == 0 :
            arr = arr[:query[i] + 1]
        else :
            arr = arr[query[i]:]
    for j in arr :
        answer.append(j)
    
    return answer

처음에

def solution(arr, query):
    answer = []
    for i in range(len(query)) :
        if i % 2 == 0 :
            arr = arr[:query[i] + 1]
            answer.append(arr)
        else :
            arr = arr[query[i]:]
            answer.append(arr)
    return answer
    
이렇게 하니까 과정이 다 리스트에 담겼다. 그래서

def solution(arr, query):
    answer = []
    for i in range(len(query)) :
        if i % 2 == 0 :
            arr = arr[:query[i] + 1]
        else :
            arr = arr[query[i]:]
    answer.append(arr)
    return answer
    
이렇게 들여쓰기를 바꾸니까 값이 [[1,2,3]] 이렇게 나오길래

def solution(arr, query):
    answer = []
    for i in range(len(query)) :
        if i % 2 == 0 :
            arr = arr[:query[i] + 1]
        else :
            arr = arr[query[i]:]
    for j in arr :
        answer.append(j)
    
    return answer

이렇게 반복문을 돌려서 리스트의 값을 빼내서 answer리스트에 넣으면 되겠다 싶어서 반복문을 돌렸다.

반복문 돌릴 필요 없이 return arr 하면 되는 문제였다.

arr[x:y]는 인덱스 x부터 y 전까지의 값을 갖겠다라는 뜻이다. 버리겠다가 아니라.
