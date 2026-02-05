def solution(a, b):
    if a % 2 == 1 and b % 2 == 1 :
        return a*a + b*b
    elif a % 2 == 1 and b % 2 == 0 :
        return 2 * (a + b)
    elif a % 2 == 0 and b % 2 == 1 :
        return 2 * (a + b)
    else :
        return abs(a - b)
======================================
abs() 절대값을 반환해주는 함수

def solution(a, b):
    if a % 2 == 1 and b % 2 == 1 :
        return a*a + b*b
    elif a % 2 == 1 or b % 2 == 1 :
        return 2 * (a + b)
    else :
        return abs(a - b)
이렇게 or를 써서 두번째와 세번째 단을 합쳐서 쓸 수 있다.
