def solution(num_list):
    if num_list[-1] > num_list[-2] :
        num_list.append(num_list[-1] - num_list[-2])
    else :
        num_list.append(num_list[-1] * 2)
    return num_list

append 뒤엔 ()가 붙는다. 까먹지 말자.
마지막 인덱스를 묻는 문제니까 [-1]로 마지막 인덱스를 찾아주고
[-2]로 그 전 인덱스만 찾으면 쉽게 풀린다.
