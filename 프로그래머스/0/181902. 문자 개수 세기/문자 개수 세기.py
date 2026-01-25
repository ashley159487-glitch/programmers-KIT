def solution(my_string):
    answer = [0] * 52
    
    for i in my_string :
        big = ord(i) - ord("A")
        small = ord(i) - ord("a") + 26
        if i.isupper() :
            answer[big] += 1
        elif i.islower() :
            answer[small] += 1
    return answer