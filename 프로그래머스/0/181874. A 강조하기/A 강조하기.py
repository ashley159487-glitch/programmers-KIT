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