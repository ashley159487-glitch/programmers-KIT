def solution(my_string, m, c):
    answer = ''
    for i in range(c - 1, len(my_string), m) :
        answer += my_string[i]
    return answer

range(a, b, c) : 에서
a는 시작하는 인덱스
b는 끝 인덱스
c는 step 즉 c만큼 뛰어서 나온 인덱스를 나타낸다.
이건 for문 처음 배울 때 배운 건데 잘 안 쓰다보니까
실전에서 떠올리기 쉽지 않다. 
"일정한 간격(N배수, 격자무늬, 세로줄)" 문제를 만날 때 이 step은 강력한 치트키가 된다.
알아두자.

"N번째 마다", "N글자씩 건너뛰며"라는 문구가 보이면 무조건 range의 세 번째 인자인 step을 먼저 떠올리자.
