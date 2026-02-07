def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1) :
        if phone_book[i+1].startswith(phone_book[i]) :
            return False
    return answer
========================================================
배열의 값들을 정렬 후 반복문을 돌려 앞의 인덱스의 접두사가 뒤의 인덱스인지 확인하면 된다.
주의 할 점은 반복문의 길이를 phone_book으로 하면 맨 마지막 인덱스를 그 뒤랑 검사하려해서 오류가 나기 때문에
범위를 -1로 해줘야 한다. 그렇게 하면 startswith로 쉽게 접두사인지 확인 할 수 있다.
