def solution(strArr):
    answer = []
    for i, j in enumerate(strArr) :
        if i % 2 == 0 :
            j = j.lower()
            answer.append(j)
        else :
            j = j.upper()
            answer.append(j)
    return answer
========================================
enumerate 함수로 인덱스와 값을 동시에 뽑아내서
비교하면 쉽게 풀 수 있다.
