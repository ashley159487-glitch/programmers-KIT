def solution(arr, k):
    answer = []
    for i in arr :
        if i not in answer :
            answer.append(i)
        if len(answer) == k :
            break
    while len(answer) < k :
        answer.append(-1)
    return answer
=================================
중복을 없애는 문제라 set() 을 써야 할 거 같지만
문제를 자세히 보면 순서대로 저장되어야 하기 때문에
set을 넣는 순간 답이 다 틀리게된다.
그러므로 not in으로 중복된 값들은 넣지 말고
배열의 길이가 k와 같을 때 탈출시킨다.
그리고 배열의 길이가 k보다 작을 때 if를 써서 -1을 추가시키려고 하면
단 하나만 추가가 되므로 while문을 써서 k의 길이와 같아질 때까지 넣어줘야 한다.
while문을 쓸 때는 for문의 바깥에 써줘야 값이 정확하게 들어가게 된다.
