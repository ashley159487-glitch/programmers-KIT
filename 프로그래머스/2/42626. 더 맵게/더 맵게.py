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
==================================================
슬슬 문제를 보면 어느정도 그 길이 머릿속에 그려지긴 한다.
이 문제는 힙 라이브러리로만 풀수있게 강요된 문제라 sort와 리스트로 방향은 잡을 수 있지만 풀 수는 없다.
여기서 쓴 힙 메서드들을 정리하자면
heapify(list) : 리스트를 힙 구조로 바꿈
heappop(list) : 리스트에서 가장 작은 값을 꺼냄
heappush(list, 값) : 값을 리스트에 집어넣음(자동으로 순서를 맞춰서 들어감)
이렇게 있다.
먼저 heapify로 리스트를 힙 구조로 바꾼 후 카운트 할 변수를 만들어준다.
반복문으로 가장작은 값과 그 다음 값을 heappop으로 빼주는데 여기서 주의할 점은 리스트 내에 값이 최소
두개는 있어야 에러가 안나므로 조건부터 걸어준다. 그다음 식대로 계산해준 후 카운트를 올리고 리스트에 다시 값을 집어넣어준다.
else로 예외상황(다 더했는데도 K보다 작을 때) -1을 리턴시켜준다.
