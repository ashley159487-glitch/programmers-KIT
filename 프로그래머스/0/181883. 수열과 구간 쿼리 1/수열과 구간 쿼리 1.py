def solution(arr, queries):
    answer = []
    for i in range(len(arr)) :
        for j in queries :
            if j[0] <= i <= j[1] :
                arr[i] = arr[i] + 1
                
    return arr
=======================================
def solution(arr, queries):
    answer = []
    for i in range(len(arr)) :
        for j in queries :
            if j[0] <= i <= j[1] :
                arr[i] = arr[i] + 1
                answer.append(arr[i])
                
    return answer

처음 썼던 코드다. 이 코드를 출력 시키는 시뮬레이션은 이렇게 된다.
i = 0 일 때:
queries 중 [0, 1]에 해당함 → arr[0]이 1이 됨 → answer.append(1) → answer = [1]
i = 1 일 때:
queries 중 [0, 1]에 해당함 → arr[1]이 2가 됨 → answer.append(2) → answer = [1, 2]
queries 중 [1, 2]에 해당함 → arr[1]이 3이 됨 → answer.append(3) → answer = [1, 2, 3]
(벌써 i=1 하나 때문에 값이 2개나 들어갔죠?)
i = 2 일 때:
queries 중 [1, 2]에 해당함 → arr[2]가 3이 됨 → answer.append(3) → answer = [1, 2, 3, 3]
queries 중 [2, 3]에 해당함 → arr[2]가 4가 됨 → answer.append(4) → answer = [1, 2, 3, 3, 4]
i = 3 일 때:
queries 중 [2, 3]에 해당함 → arr[3]이 4가 됨 → answer.append(4) → answer = [1, 2, 3, 3, 4, 4]

즉 arr안의 결괏값만 바꾸면 되는데 그 바뀌는 과정을 하나하나 answer에 append하니 답이 틀릴 수 밖에 없었다.
문제를 보면 queries를 처리한 이후의 arr를 return 하는 이라고 명시되어있다.
즉 반복을 돌려서 answer에 append하는 게 아니라 바로 arr을 return하라고 친절하게 설명해줬는데
내가 문제를 대충 읽어서 생긴 문제라고 볼 수 있다.
