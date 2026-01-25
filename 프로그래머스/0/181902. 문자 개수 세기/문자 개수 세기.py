def solution(my_string):
    answer = [0] * 52
    
    for i in my_string :
        big = ord(i) - ord("A")
        small = ord(i) - ord("a") + 26
        if i.isupper() :
            answer[big] += 1
        elif i.islower() :
            answer[small] += 1
    return answer

.isupper() : 대문자인지 구분하는 함수
.islower() : 소문자인지 구분하는 함수

너무 오랜만에 아스키코드를 사용하는 문제를 봤다.
ord("문자열") 이렇게 하면 그 문자열에 대입되어있는 숫자를 알 수 있다.
그리고 이 문제는 최종적인 리스트의 인덱스의 수를 알 수 있기 때문에
미리 0으로 52자리를 만들어 놓고 시작한다.
my_string을 for문으로 반복 할 때
변수를 만들어 ord(i) - ord("A") 를 넣는다. 그러면 i가 A일 때 0, B일 때 1
이렇게 숫자가 나오게 된다.
그리고 if문으로 이 i가 대문자인지 소문자인지 판단 후 answer[](answer변수의 인덱스에) 집어 넣는다.
그리고 같은 문자가 나오면 숫자를 누적 시켜야 하기에 += 1을 한다.
소문자의 경우 이미 앞에서 대문자의 인덱스가 0 ~ 25이기 때문에 선언 한 변수의 뒤에 + 26을 해줘서
26부터 집어넣게 만든다.
