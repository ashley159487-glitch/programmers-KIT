def solution(arr):
    stk = []
    i = 0
    while i < len(arr) :
        if not stk :
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i] :
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i] :
            del stk[-1]
    return stk

처음에 반복문을 뭘 쓸지 가닥만 잡으면 문제의 지문대로
코드를 쓰면 맞출 수 있는 문제.

반복 할 횟수가 정해져 있다 : for
횟수가 정해져있지 않다 : while
이걸 기억하자. 처음에 for문으로 만들어봤을 때 뒤에 길이를 넣을만한 변수가 없으면
while문으로 쓰자.
