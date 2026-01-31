def solution(myString, pat):
    for i in range(len(myString), 0, -1) :
        if myString[:i].endswith(pat) :
            return myString[:i]
=============================================
endswith함수의 경우 한 문자 뿐 아니라 접미사 자체를 검사하는 것이므로
if myString[:i].endswith(pat) 이렇게 코드를 적으면 한단어 한단어 검사하는 것이 아니라
pat의 값이 되는 문자와 맞는지를 검사하므로 슬라이싱으로 나타내는 것이 적당하다.
그리고 위의 문제의 경우 접미사를 가진 가장 긴 문자열을 반환하는 것이기 때문에
뒤에서부터 거꾸로 반복시키는 것이 핵심이다.
        
        
            
    
