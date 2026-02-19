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
=========================================================
permutations(대상, 길이) 소수찾기 때도 썼지만 다시 얘기하자면
permutations를 쓰면 n! 만큼 경우의 수들을 다 만들어준다.
이 문제에서 던전 2차원배열의 각 행은 [필요 피로도, 소모피로도] 이렇게 고정되어있으므로
언패킹으로 각 값을 꺼내서 내 피로도와 필요 피로도를 비교해준다.
조건이 맞으면 던전을 돌고 카운트를 올려준다. 이것을 계속 반복하면서 최대 카운트를 계속
변수에 담아준다.
