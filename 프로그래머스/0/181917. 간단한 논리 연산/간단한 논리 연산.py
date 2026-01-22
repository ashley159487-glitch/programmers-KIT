def solution(x1, x2, x3, x4):
    answer = True
    if (x1 or x2) and (x3 or x4) :
        return answer
    else :
        return False

논리 연산이 나올 땐 항상 기억해두자!

and는 두 개가 True여야 True, or는 둘 중 하나라도 True면 True.
