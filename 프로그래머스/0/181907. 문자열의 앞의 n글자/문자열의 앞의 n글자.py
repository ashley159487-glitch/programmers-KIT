def solution(my_string, n):
    answer = ''
    a = my_string[:n]
    answer += a
    return answer

오늘의 첫 문제는 상쾌하게 시작하네.
잊을 수 있으니 슬라이싱 tip을 적어놓자면

my_string[:n]: 처음부터 n-1 인덱스까지 (총 n글자)
my_string[n:]: n 인덱스부터 끝까지
my_string[-n:]: 뒤에서부터 n글자

이렇게 알고있으면 된다.
