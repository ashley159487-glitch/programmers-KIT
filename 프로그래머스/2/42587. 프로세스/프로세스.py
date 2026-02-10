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