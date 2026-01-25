def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)) :
        if i not in indices :
            answer += my_string[i]
    return answer

not in을 써서 인덱스를 거르고, 남아있는 인덱스의 글자들만 이어 붙인다.
