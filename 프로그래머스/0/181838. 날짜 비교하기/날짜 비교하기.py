def solution(date1, date2):
    if date1 < date2 :
        return 1
    else :
        return 0
===============================
파이썬에서는 리스트끼리의 크기 비교도 가능하다.
원래는 각각 언패킹해서 if문으로 하나하나 비교하려고 했는데
그럴 필요 없이 date2가 date1보다 클 때만 1을 리턴시키면 된다.
