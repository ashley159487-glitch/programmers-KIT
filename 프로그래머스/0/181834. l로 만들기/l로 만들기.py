def solution(myString):
    answer = ''
    for i in myString :
        if i < "l" :
            answer += "l"
        else :
            answer += i
    return answer
============================
파이썬이나 자바나 모두 알파벳을 아스키코드 숫자로 저장하고 있기 때문에
알파벳끼리의 대소비교가 가능하다.
그걸 이용하면 쉽게 풀린다.
