def solution(s):
    cnt = 0
    for i in s :
        if i == '(' :
            cnt += 1
        else :
            cnt -= 1
        if cnt < 0 :
            return False
    if cnt < 0 or cnt > 0 :
        return False
    else :
        return True
===============================
접두사 접미사만 중요한 게 아니라 문자열 내 괄호들이 모두 닫혀있는지 확인하는 문제이기 때문에
( 가 나오면 +1 ) 가 나오면 -1 해서 총 계산 한 값이 0이 나오면 True를 return하게 해야하는데
주의점은 맨 처음 만나는 문자가 )로 시작할 때 바로 False를 리턴하게 해야한다.
    
