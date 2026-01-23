def solution(my_string, is_suffix):
    if my_string.endswith(is_suffix) :
        return 1
    else : 
        return 0

접미사인지 확인하는 함수 : endswith()
접두사인지 확인하는 함수 : startswith()

인덱스 슬라이싱으로도 하는 방법이 있다.

def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix :
        return 1
    else : 
        return 0

이렇게하면 위의 함수들을 몰라도
답을 낼 수 있다.
