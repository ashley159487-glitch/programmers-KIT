def solution(priorities, location):
    queue = []
    for i, j in enumerate(priorities) :
        queue.append((j, i))
    cnt = 0
    while queue :
        p = queue.pop(0)
        if queue and p[0] < max(i[0] for i in queue) :
            queue.append(p)
        else :
            cnt += 1
            if p[1] == location :
                return cnt
=========================================================
이 문제에서 가장 중요한 것은 먼저 각각의 인덱스에 순서를 매겨서 저장시켜야 한다는 것.
priorities 이 리스트를 그대로 사용하는 것이 아니라 이 리스트 안의 값들의 인덱스를 1대1로 값과 매칭시켜서 저장시켜야 문제가 풀린다.
그 저장시킨 리스트의 길이를 나는 모르기 때문에 while문으로 반복을 돌리고, 기준점 하나를 빼내 변수에 저장시킨다.
여기서 두번째 중요 포인트는 queue리스트 안에 값이 하나라도 있어야 조건문을 실행시켜야 한다는 점.
그러므로 if queue and로 리스트에 값이 있을 때만 기준점을 최대값이랑 비교시킨다.
기준점이 작으면 리스트의 마지막에 추가시키고 이걸 반복하다가 기준점이 최대값과 같을 때 cnt를 +1해준다.
그리고 그 최대값이 location(내가 확인해야하는 프로세스의 인덱스의 위치)와 같다면 그 때 cnt를 리턴해준다.
