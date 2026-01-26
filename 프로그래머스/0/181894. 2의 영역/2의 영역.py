def solution(arr):
    answer = []
    indexes = []
    for i in range(len(arr)) :
        if arr[i] == 2 :
            indexes.append(i)
    if len(indexes) == 0 :
        return [-1]
    start = indexes[0]
    end = indexes[-1]
    answer = arr[start:end + 1]
            
            
    return answer
시작을    
for i in range(len(arr)) :
        if arr[i] == 2 :
로 하고 막혔다.

이 문제는 코드에서 보다시피 arr의 리스트 안에서
2인 값들의 인덱스 번호를 뽑아 변수에 담고
그 변수로 arr을 잘라야 했다.
이걸 모르니 처음부터 막힐 수 밖에 없었다.
이런 발상을 하려면 어떻게 해야하지...
