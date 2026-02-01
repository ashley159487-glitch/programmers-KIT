def solution(myString, pat):
    answer = ""
    for i in myString :
        if i == "A" :
            answer += "B"
        else :
            answer += "A"
    if pat in answer :
        return 1
    else :
        return 0
=====================================
문자열 치환은 이제 머릿속에 그려지는 문제다.
간단하게 풀었다.
