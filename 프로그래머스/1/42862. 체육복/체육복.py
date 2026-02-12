def solution(n, lost, reserve):
    r_lost = set(lost) - set(reserve)
    r_reserve = set(reserve) - set(lost)
    
    for i in sorted(r_reserve) :
        if i - 1 in r_lost :
            r_lost.remove(i - 1)
        elif i + 1 in r_lost :
            r_lost.remove(i + 1)
    return n - len(r_lost)


# 각 리스트에서 중복되는 값들을 지워준다
