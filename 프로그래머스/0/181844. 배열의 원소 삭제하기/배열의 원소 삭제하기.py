def solution(arr, delete_list):
    answer = []
    for i, j in enumerate(arr) :
        if j not in delete_list :
            answer.append(j)
    
    return answer
===================================
주어진 두 리스트의 길이가 다를 경우
==, !=를 써서 비교할 수 없다.
in을 써서 한 리스트의 안에 값이 들어있는지 확인하자.
