def solution(arr):
    answer = []
    for i in arr :
        if i >= 50 and i % 2 == 0 :
            answer.append(i // 2)
        elif i < 50 and i % 2 == 1 :
            answer.append(i * 2)
        else :
            answer.append(i)
    return answer
=======================================
처음에는 else부분을 안 쓰고 코드를 실행했다가 틀려서 다시 문제를 보니까
해당이 안되는 수도 출력되야 한다길래 else를 썼다.
문제를 잘 읽는 습관을 기르자 이 말만 몇번을 쓰는지 모르겠다...
코드에 관해서는 정수가 나와야하니까 나누기를 // 로 써야한다는 것이다.
그냥 / 만 하면 실수로 표현되기 때문에 무조건 // 로 쓰자.
