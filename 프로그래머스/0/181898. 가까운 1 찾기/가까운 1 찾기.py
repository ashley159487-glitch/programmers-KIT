def solution(arr, idx):
    answer = 0
    for i in range(len(arr)) :
        if arr[i] == 1 and i >= idx :
            return i
    return -1

arr은 수의 배열이므르 list형이다. 그러므로 range(arr)로 하면 오류가 난다.
배열을 반복문으로 돌릴 때는 range(len(arr)) 이렇게 len() 를 쓰자.
문제를 보면 가장 작은 인덱스를 찾는 것이므로, 끝까지 반복을 돌리면 안된다.
if문으로 조건을 걸고 그 조건에 해당하는 인덱스가 되자마자 반복을 종료시켜야 하므로
answer변수에 담지 말고 바로 return i를 해야 끝까지 반복이 안돈다.
else를 쓸 필요 없이 for문 밖에 return -1를 하면 인덱스가 없으면 -1를 return하게 된다.

이거랑 별개로 문제가 이상해서 정상적인 답 i > idx일 때 정답처리가 안된다.
