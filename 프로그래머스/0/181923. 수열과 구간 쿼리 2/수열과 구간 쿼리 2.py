def solution(arr, queries):
    answer = []
    for s, e, k in queries :
        c = []
        for i in range(s, e + 1) :
            if arr[i] > k :
                c.append(arr[i])
        if c :
            answer.append(min(c))
        else :
            answer.append(-1)
            
    return answer

이 문제는 손도 못댔다...
일단 queries안의 s, e, k 값을 각각 알아내야 하기 때문에 for문을 돌리고, 
그다음엔 돌려서 나온 그 값들을 arr[i]랑 비교해야하기 때문에 for문을 또 돌린다.
문제에
각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.
이렇게 써져있으므로 s부터 e + 1까지의 범위만큼 반복문을 돌리고, 그 안에서 arr[i]가 k보다
큰 수들을 찾고, for문을 빠져나와 if문으로 가장 작은 arr[i]를 찾아 return한다.
만약 k보다 큰 수가 없다면 -1를 return해야 하므로 else문에서 -1을 return하게 append한다.

"미션 목록을 도는 큰 루프 안에서, 각 미션이 정해준 범위(s~e)만큼만 움직이는 작은 루프를 실행하는 '중첩 반복문' 구조가 핵심이다."
