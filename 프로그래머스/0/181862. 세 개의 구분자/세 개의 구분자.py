import re
def solution(myStr):
    answer = []
    for i in re.split(r'[abc]', myStr) :
        if i != "" :
            answer.append(i)
    return answer if answer else ["EMPTY"]
=============================================
이렇게 re를 import해서 한번에 a, b, c를 기준으로 자르는 방법도 있고
==============================================
def solution(myStr):
    answer = []
    charList = ['a', 'b', 'c']
    for i in charList :
        myStr = myStr.replace(i, " ")
    answer = myStr.split()
    return answer if answer else ["EMPTY"]
===============================================
이렇게 a, b, c를 담은 리스트를 만들고 for문으로 돌려서 replace후
split하는 방법도 있다.
