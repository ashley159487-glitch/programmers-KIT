def solution(board, k):
    answer = 0
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            if i + j <= k :
                answer += board[i][j]
    return answer
===========================================
문제대로 코드를 만들면 되는데 주의할 점이 있다.
두번째 for문의 range에 len(board)를 넣게 되면 런타임 오류나 실패가 뜬다.
왜냐하면 len(board)의 길이와 len(board[i])의 길이가 다를 수 있기 때문이다.
이 것만 유념하면 문제대로 코드를 만들면 바로 풀린다.
