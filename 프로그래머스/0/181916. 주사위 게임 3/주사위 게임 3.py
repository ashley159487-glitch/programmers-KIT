def solution(a, b, c, d):
    answer = 0
    dice = sorted([a, b, c, d])
    
    if dice[0] == dice[3] :
        p = dice[0]
        answer = 1111 * p
    elif dice[0] == dice[2] :
        p = dice[0]
        q = dice[3]
        answer = (10 * p + q) ** 2
    elif dice[1] == dice[3] :
        p = dice[1]
        q = dice[0]
        answer = (10 * p + q) ** 2
    elif dice[0] == dice[1] and dice[2] == dice[3] :
        p = dice[0]
        q = dice[2]
        answer = (p + q) * abs(p - q)
    elif dice[0] == dice[1] :
        p = dice[0]
        q = dice[2]
        r = dice[3]
        answer = q * r
    elif dice[1] == dice[2] :
        p = dice[1]
        q = dice[0]
        r = dice[3]
        answer = q * r
    elif dice[2] == dice[3] :
        p = dice[2]
        q = dice[0]
        r = dice[1]
        answer = q * r
    elif dice[0] != dice[3] :
        answer = min(dice)
    
    return answer