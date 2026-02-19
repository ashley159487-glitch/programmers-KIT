from itertools import permutations
def solution(k, dungeons):
    max_cnt = 0
    for p in permutations(dungeons, len(dungeons)) :
        cnt = 0
        real_k = k
        for i, j in p :
            if real_k >= i :
                real_k = real_k - j
                cnt += 1
                if real_k < j :
                    break
        if max_cnt < cnt :
            max_cnt = cnt
    return max_cnt