def solution(num_list):
    answer = 0
    for i in range(len(num_list)) :
        if num_list[i] < 0 :
            return i
    return -1

처음에는
for i in num_list :
    if i % 2 == 0 or i % 2 == 1 :
        return -1
    else :
        return i
이렇게 썼는데 % 2를 하는 건 홀짝을 찾을 때고, 음수를 찾는 건 i < 0 이다.
알고 있었는데... 왜 생각이 전혀 안났지...
어쨌든 그 후에
for i in num_list :
    if i < 0 :
        return ...
    else :
        return -1
이렇게 짰는데 저 ...자리에 뭘 넣어야 할지 모르겠었다.
i도 아니고 num_list[i]도 아니고

결국 인덱스를 구하기 위해선 인덱스 값을 뽑아내야 한다는 걸 알게됐고,
for i in range(len(num_list)) :
        if num_list[i] < 0 :
            return i
        else :
            return -1
이렇게 짰는데 값이 다 -1이 찍혔다.
문제점이 뭐였냐면 for문에 0번째 인덱스를 확인 할 때 음수가 아니기 때문에
else로 넘어가 -1을 return했기 때문이었다.
이 문제를 해결하기 위해선 else가 아니라 for문 밖에 return -1를 해야한다.

결론을 내리기 전에 모든 데이터를 다 훑었는지 확인하자. 성급한 else는 버그의 지름길이다.
