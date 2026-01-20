def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)) :
        c = numLog[i] - numLog[i-1]
        if c == 1 :
            answer += 'w'
        elif c == -1 :
            answer += 's'
        elif c == 10 :
            answer += 'd'
        elif c == -10 :
            answer += 'a'
    return answer

수 조작하기1 문제의 역버전인데...
변수[i] - 변수 [k] 는 인덱스의 번호를 구하는 게 아니라
각 인덱스의 해당 값끼리 연산 하는 거다.
인덱스를 대입해서 풀어야 하므로 for문도 range와 len을 써서 변수의 길이만큼 반복해야 한다.
