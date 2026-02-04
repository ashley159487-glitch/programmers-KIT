def solution(sizes):
    max_w = 0
    max_h = 0
    for w, h in sizes :
        big = max(w, h)
        small = min(w, h)
        if big > max_w :
            max_w = big
        if small > max_h :
            max_h = small
    return max_w * max_h
=============================
이 코드를 해석하면 반복문을 돌려서 [w, h]값을 가진 값들을 뽑고 
첫번째 리스트의 큰 값을 big에 작은 값을 small에 넣고 
각각 if문으로 max_w랑 max_h에 넣은 후 그다음 리스트 반복으로 넘어가
전 값들이랑 비교해서 큰 값들만 남겨 result한다.

일단 기초문제가 아닌 알고리즘 kit문제들은 문제부터 길기 때문에
천천히 읽고 문제를 해석하는 능력을 길러야한다.
