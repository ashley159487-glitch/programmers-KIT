import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K :
        if len(scoville) >= 2 :
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new = first + (second * 2)
            cnt += 1
            heapq.heappush(scoville, new)
        else :
            return -1
    return cnt

# heapify로 리스트를 힙 구조로 바꿈
# heappop을 두번 실행해서 가장작은 값, 그다음 값을 꺼내고 계산하기
# heappush로 값을 넣기