def solution(citations):
    cnt = 0
    citations.sort(reverse = True)
    for i, j in enumerate(citations) :
        if j >= i + 1 :
            cnt += 1
    return cnt

