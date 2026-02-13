def solution(citations):
    cnt = 0
    citations.sort(reverse = True)
    for i, j in enumerate(citations) :
        if j >= i + 1 :
            cnt += 1
    return cnt
============================================
코드만 보면 그리 어려운 느낌이 아닌데 문제 자체가 난해해서 문제 이해에만 많은 시간을 쏟아야 할 거 같은 문제이다.
정리하자면 각 값을 내림차순으로 정렬하여 각 값이 자기 순서의 숫자보다 작아지기 전 까지 카운트 해줘야 한다.

