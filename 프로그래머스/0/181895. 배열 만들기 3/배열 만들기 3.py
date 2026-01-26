def solution(arr, intervals):
    answer = []
    for i in intervals :
        a, b = i
        for j in range(a, b + 1) :
            answer.append(arr[j])
            
    return answer

문제를 보고 2중for문으로 intervals안의 리스트의 각각의 값들을
빼내서 arr을 슬라이싱 하려고 했다.

for i in intervals :
    for j in i :
        answer = arr[j[
이렇게 뭘 써야할지 모르겠어서 질문하기를 봤다.
거기엔 처음의 코드가 있었고, 이해가 되질 않았다.
intervals를 반복문으로 돌려서 빼냈으면
그 값은 각각 2개의 값이 들어있는 리스트형식인데
왜 그 다음 for문을 돌릴 때 range(a, b + 1) 이게 되는거지?
이걸 풀어보면 range([a,b], [a1,b1] + 1) 아닌가? 라고 생각됐다.
이해가 안가 제미나이에게 물어보니 a, b = i는 i에 각각 리스트를 담는게 아니라,
리스트 안의 값을 각각 a와 b에 넣는 작업이라고 했다.
그래서 다음 for문 안에 각각의 숫자가 들어올 수 있었던 거고 arr[j]로 슬라이싱해서
answer에 그 값을 넣을 수 있던 거였다.

데이터 뭉치(i)를 다룰 때, 그 안의 알맹이가 몇 개인지 안다면 언패킹(a, b = i)을 통해 반복문 없이 바로 숫자로 꺼내 쓸 수 있다.
언패킹 없이 인덱스 직접 접근(i[0], i[-1] + 1)으로도 범위 설정이 가능하다.
def solution(arr, intervals):
    answer = []
    for i in intervals :
        for j in range(i[0], i[-1] + 1) :
            answer.append(arr[j])
이렇게 사용 가능.
