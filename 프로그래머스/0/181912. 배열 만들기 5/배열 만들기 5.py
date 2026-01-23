def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs :
        sli = int(i[s:s + l])
        if sli > k :
            answer.append(sli)
    return answer

아직은 슬라이싱이 서툴다...
그래도 계속 이런 문제들을 풀다 보니까
틀을 어떻게 잡아야 하는지 감이 잡히기 시작하는 듯 하다.
