def solution(myString, pat):
    answer = 0
    for i in range(len(myString)) :
        if myString[i:i + len(pat)] == pat :
            answer += 1
    return answer
================================================
인덱싱의 또 다른 응용문제가 나오니 다시 헤매는 꼴이 나왔다.
이 문제의 경우 인덱싱을 이용해 한칸씩 뒤로 가며 모든 문자열을 pat의 값과 비교를 해야하기 때문에
for문의 step을 len(pat)으로 잡을 경우 중간의 단어들을 검사를 못한다.
무조건 한 칸씩 검사를 하되, myString[i:i + len(pat)] 이렇게 슬라이싱 해서
모든 문자열 안의 경우의 수들을 검사해야 한다.
