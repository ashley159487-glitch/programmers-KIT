def solution(brown, yellow):
    
    wide = brown + yellow
    for i in range(3, int(wide**0.5) + 1) :
        if wide % i == 0 :
            j = wide // i
            if (j - 2) * (i - 2) == yellow :
                return [j, i]