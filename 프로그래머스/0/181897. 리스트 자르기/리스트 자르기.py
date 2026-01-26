def solution(n, slicer, num_list):
    answer = []
    if n == 1 :
        answer = num_list[0:slicer[1] + 1]
        
    elif n == 2 :
        answer = num_list[slicer[0]:]
        
    elif n == 3 :
        answer = num_list[slicer[0]:slicer[1] + 1]
        
    else :
        answer = num_list[slicer[0]:slicer[1] + 1:slicer[2]]
    return answer

처음에는 for문을 돌려서 slicer의 값들을 꺼내와 인덱스에 대입하려고 했는데
에러가 났다. (for a, b, c in slicer :) 이걸로
생각해 보니까 그럴 필요가 전혀 없고, 그저 slicer[]의 값들로 각 가정시 마다
잘라주면 되는 거였다....
다시 무조건적인 for문 쓰기, if문 쓰기병이 도지고 있다.
문제를 잘 보고 정말 필요한 것인지 먼저 잘 생각 해 보자.
   
