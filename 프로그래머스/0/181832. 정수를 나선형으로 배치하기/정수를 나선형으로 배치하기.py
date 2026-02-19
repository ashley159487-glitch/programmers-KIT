def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)] # n길이만큼 0으로 채워진 2차원 배열을 만든다.
    
    #행과 열의 변화를 만들어줄 설명서를 만든다.
    dr = [0, 1, 0, -1] # 행의 변화(0 : 우, 1 : 하, 0 : 좌, -1 : 상)
    dc = [1, 0, -1, 0] # 열의 변화(1 : 우, 0 : 하, -1 : 좌, 0 : 상)
    
    #현재 위치와 바라보는 위치를 가리켜 줄 변수를 만든다.
    #처음에는 (0, 0), 오른쪽을 바라보게 한다.
    r = 0
    c = 0
    dist = 0

    #1부터 n*n까지 숫자를 적으며 전진시킨다.
    for i in range(1, n * n + 1) :

        #현재 있는 칸(r, c)에 i를 적는다
        answer[r][c] = i

        #가장 중요! 가야할 곳을 그냥 가는게 아니라 변수를 만들어 미리 계산 해본다.
        nr = r + dr[dist]
        nc = c + dc[dist]

        #배열의 밖으로 빠져나가진 않는지, 가는 곳이 0인지 아닌지를 판별시킨다.
        if nr < 0 or n <= nr or nc < 0 or nc >= n or answer[nr][nc] != 0 :

            #위의 판별에 해당하는 경우 핸들을 90도 꺾는다.
            dist = (dist + 1) % 4

            #꺾은 방향이 갈 수 있는 길인지 확인한다.
            nr = r + dr[dist]
            nc = c + dc[dist]
        
        #갈 수 있는 길이면 이제 진짜 간다.
        r = nr
        c = nc
    return answer
