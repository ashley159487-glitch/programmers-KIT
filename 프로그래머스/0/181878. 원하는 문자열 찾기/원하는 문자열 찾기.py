def solution(myString, pat):
    if pat.lower() in myString.lower() :
        return 1
    else :
        return 0
============================================
단, 알파벳 대문자와 소문자는 구분하지 않습니다. 이런 문구가 있으면
무조건 소문자던 대문자던 통일을 시키자...
근데 구분하지 않는다고 하면 보통 상관없다는 뜻 아닌가...?
lower() 소문자로 변경
upper() 대문자로 변경
