def solution(prices):
    answer = []
    
    for i in range(len(prices)) :
        cnt = 0
        for j in range(i + 1, len(prices)) :
            if prices[i] <= prices[j] :
                cnt += 1
            else :
                cnt += 1
                break
        answer.append(cnt)
    return answer
==================================================
2중for문으로 각 인덱스를 기준으로 삼아서 뒤의 값과 크기 비교를 해준다.
주의할 점은 크기 비교를 할 때는 이미 1초가 지나간 것이므로 뒤의 값이 크기가 작아도 cnt는 +1해준다.
두번째 for문에서 시작점을 잡을 때는 처음 for문의 i + 1을 해줘야 각 인덱스의 뒤의 값들과 비교가 가능하다.
만약 1, len(prices)라고 써놓으면 1번인덱스부터 비교하게된다.
