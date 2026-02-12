def solution(n, lost, reserve):
    r_lost = set(lost) - set(reserve)
    r_reserve = set(reserve) - set(lost)
    
    for i in sorted(r_reserve) :
        if i - 1 in r_lost :
            r_lost.remove(i - 1)
        elif i + 1 in r_lost :
            r_lost.remove(i + 1)
    return n - len(r_lost)
==========================================
이 문제에서 가장 중요한 부분은 각 리스트에 중복되어있는 학생이 있다는 것이다.
그러므로 각각 리스트를 set타입으로 만든 후 서로를 빼주고 변수에 담아준다.
문제에서 보면 원래 학생 번호는 순서대로인데 새로 만든 변수들은 set타입이므로 수가 뒤죽박죽 섞여있다.
sorted로 reserve를 정렬해주고 반복문을 돌려준다.
반복문 안에서 조건문을 만들 때 생각해봐야 할 문제가 있다.
i가 옷을 빌려줄 때, i-1 에게 먼저 물어봐야하나 i+1 에게 물어봐야하나의 문제다.
여기서 앞의 사람은 i가 아니면 옷을 구할 방법이 더 적기 때문에 i - 1이 lost리스트 안에 있는지부터 따진 후
있으면 lost리스트 안에서 지워준다.
그 후 앞의 번호에게 못 빌린 학생들만 뒷번호한테 빌릴 수 있게 elif로 조건을 잡아준다.
이렇게 반복을 끝냈으면 전체 학생수에서 최종 lost리스트의 길이만큼 빼주면 학생들의 최대값이 나온다.
