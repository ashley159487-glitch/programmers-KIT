def solution(n):
    answer = []
    answer.append(n)
    while n != 1 :
        if n % 2 == 0 :
            n = n // 2
            answer.append(n)
        else :
            n = 3 * n + 1
            answer.append(n)
    return answer

평소에 while 뒤에 True만 봐서 다른 식이 들어온 게 어색하다.
물론 True를 쓰고도 만들 수 있다.
그리고 처음에 초기값을 안넣어서 반복문 밖에 그냥 초기값을 넣고 반복을 시작했는데,
반복문 안에다가 초기값을 넣고 해도 된다.
