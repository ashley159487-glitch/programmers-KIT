def solution(n, control):
    for i in control :
        if i == 'w' :
            n = n + 1
        elif i == 's' :
            n = n - 1
        elif i == 'd' :
            n = n + 10
        else :
            n = n - 10
    return n

for문의 완전 기초를 묻는 문제.
딱히 뭘 쓰지 않아도 될 정도로 쉽다.
