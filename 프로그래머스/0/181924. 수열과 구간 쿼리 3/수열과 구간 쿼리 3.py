def solution(arr, queries):
    answer = []
    for i, j in queries :
        arr[i], arr[j] = arr[j], arr[i]
        
    return arr

여기서 queries는 arr안에 있는 수를 두 개만 꺼내서 리스트화 시킨게 아니라
arr 리스트의 인덱스 번호를 담은 리스트이다.
그러므로 arr은 놔두고 queries를 반복문을 돌려서
j와 i를 스위칭해주면 된다.
