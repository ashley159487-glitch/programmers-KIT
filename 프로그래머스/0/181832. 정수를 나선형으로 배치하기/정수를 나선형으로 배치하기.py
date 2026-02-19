def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = 0
    c = 0
    dist = 0
    for i in range(1, n * n + 1) :
        answer[r][c] = i
        nr = r + dr[dist]
        nc = c + dc[dist]
        if nr < 0 or n <= nr or nc < 0 or nc >= n or answer[nr][nc] != 0 :
            dist = (dist + 1) % 4
            nr = r + dr[dist]
            nc = c + dc[dist]
        r = nr
        c = nc
    return answer