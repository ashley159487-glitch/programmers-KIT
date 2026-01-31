def solution(myString):
    answer = ''
    for i in myString :
        if i == "a" :
            i = i.upper()
            answer += i
        elif i == "A" :
            answer += i
        else :
            i = i.lower()
            answer += i
    return answer
==============================
a일 때나 다른 문자가 나올 때의 비교문은 쉽게 떠올랐지만
A일 때 A를 출력시켜야 한다는 것을 누락시켰었다.
모든 반례를 생각 할 수는 없기에 일단 코드를 써 보고 뭐가 빠졌는지
뭐가 틀렸는지 생각 하는 것도 중요할 거 같다.
