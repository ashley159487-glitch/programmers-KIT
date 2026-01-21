def solution(l, r):
    answer = []
    for i in range(l, r + 1) :
        if set(str(i)) <= {'5', '0'} : 
            answer.append(i)
    if not answer :
        answer.append(-1)
    return answer

잊으니까 나오는 set을 다루는 문제...
set의 성격은 set안에 중복을 허용하지 않고, 순서가 없기 때문에
포함 여부를 묻는 문제에 최적이다.

처음에

     for i in range(l, r + 1) :
        if set(str(i)) <= {'5', '0'} : 
            answer.append(i)
        else :
            answer.append(-1)
이렇게 했는데 이러면 반복문 안에서 계속 돌면서 5, 0이 아닌 숫자는 -1이 계속 찍히게 된다.
그러므로 for문 밖에 if문을 만들어 answer변수가 비었을 때 -1을 넣도록 해야한다.
