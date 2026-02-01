def solution(myString):
    answer = []
    for i in sorted(myString.split("x")) :
        if i != "" :
            answer.append(i)
    return answer
==============================================
split으로 자르고 그냥 append하니까 결과값에 빈칸이 가장 먼저 정렬이 된다.
빈칸은 정렬기준에 충족되지 않으므로 빼고 리스트에 넣는다.
