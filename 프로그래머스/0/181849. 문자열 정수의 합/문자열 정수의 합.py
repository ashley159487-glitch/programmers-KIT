def solution(num_str):
    answer = 0
    for i in num_str :
        answer += int(i)
    return answer
==========================
반복문으로 꺼낸 값들은 문자열 값이므로
정수로 형변환 시켜서 더해야한다.
