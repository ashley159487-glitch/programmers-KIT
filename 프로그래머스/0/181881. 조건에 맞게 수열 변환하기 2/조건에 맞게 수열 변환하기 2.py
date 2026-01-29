def solution(arr):
    answer = 0
    while True :
        prev = arr[:]
        for i in range(len(arr)) :
            if arr[i] >= 50 and arr[i] % 2 == 0 :
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1 :
                arr[i] = arr[i] * 2 + 1
        if prev == arr :
            return answer
        answer += 1
========================================================
이거는 내일 다시 복기 하겠지만, while문 안에서 for문을 돌리면
그 for문이 언제 끝나고, 어디에 저장 되는지를 정확하게 캐치해야 풀 수 있는 문제 같다.
당장 나는 while문 안에 for문을 돌리는 것 까지는 생각 해냈지만 그 후에 어떻게
그 값을 저장하는지 몰라 막혔었다.
일단 전 문제의 응용버전인데 전 문제에서는 arr 자체를 for문으로 돌려서 값을 출력하면 됐지만
이 문제의 경우 그 값들을 변경한 횟수를 구하다가 값들이 변하지 않을 때의 횟수를 return해야하기 때문에
for문에서 나온 값들을 바로바로 바꿔줘서 그 전값과 비교를 하고, 만약 같지 않으면 횟수를 +1해줘야 한다.
