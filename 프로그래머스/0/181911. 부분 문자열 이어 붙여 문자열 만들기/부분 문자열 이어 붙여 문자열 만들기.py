def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)) :
        q = my_strings[i]
        k = q[parts[i][0]:parts[i][1] + 1]
        answer += k
    return answer

아직도!!! 문자열을 직접 꺼내야하는 문제인지, 그 길이를 꺼내야 하는 문제인지
구분 못하면 어떻게 하냐!!!
enumerate도 배워놓고 쳐 까먹고...
문제의 의도를 잘 파악해도 처음 출발하는 방향이 달라진다.
