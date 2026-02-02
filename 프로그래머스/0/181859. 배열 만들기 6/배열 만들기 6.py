def solution(arr):
    answer = []
    for i in range(len(arr)) :
        if not answer :
            answer += [arr[i]]
        elif answer[-1] == arr[i] :
            answer = answer[:-1]
        else :
            answer += [arr[i]] 
    return answer if answer else [-1]
==========================================
이미 for문에서 루프가 돌 때마다 i 가 자동으로 증가하기 때문에
if문에서 len(arr) 을 쓸 필요가 없다.
if answer == [] : 이거보다 if not answer :
이게 더 파이썬다운 방식이다.
answer += [arr[i]] 를 answer.append(arr[i])로 바꿀 수 있고,
answer = answer[:-1]이거를 answer.pop() 로 바꿀 수 있다.
원래 마지막 조건을
  elif answer[-1] != arr[i] :
            answer += [arr[i]] 
이렇게 썼었는데 어차피 배열 안에 값들이 들어있으면 arr[i]와 같거나 다름 둘 중 하나이므로
else만 써도 된다.
