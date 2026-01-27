def solution(num_list, n):
    
    num_list = num_list[n-1:]
        
    return num_list

처음엔

def solution(num_list, n):
    
    num_list = num_list[n:-1]
        
    return num_list

이렇게 쓰니까 결과가 다르게 나왔다.
리스트의 슬라이싱을 그새 까먹고 전혀 다른 범위를 지정 한 것이다.
n번째 부터 마지막 원소까지니까
n-1로 인덱스를 맞춰주고 뒤에 아무것도 안 써주면 끝까지 출력시킨다.
왜 아는 걸 응용을 못하지...
진정 안다고 하는 것은 그냥 머리로 이해하는 게 아니라 도구로써 활용 하는 것이
진정 아는 것이다.
