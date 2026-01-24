def solution(q, r, code):
    answer = ''
    for i in range(len(code)) :
        if i % q == r :
            answer += code[i]
    return answer

enumerate를 써도 된다.
    
주어진 정수값을 토대로 슬라이싱해도 된다.

전 문제인 세로 읽기 문제의 경우
"~번째"라는 말이 나오기 때문에 - 1을 고민해야 한다.
이번 문제는
"나머지가 ~인 인덱스"처럼 직접 숫자 규칙을 주기 때문에 그 숫자 그대로 쓰면 된다.
