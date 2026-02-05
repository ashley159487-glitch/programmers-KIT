def solution(picture, k):
    answer = []
    for i in picture :
        first = ""
        for j in i :
            first += j * k
        for e in range(k) :
            answer.append(first)
    return answer
==================================
2중 for문을 사용해서 문자열로 집어넣고 그걸 리스트형 변수에 넣는 것 까지는
생각을 했는데 밑에 for문을 한 번 더 사용해서 k의 길이만큼 append하는 건 생각을 못했다.
그리고 변수를 반복문 밖, 2중for문 안에밖에 설정을 안해봐서 계속 값이 엉뚱하게 튀었다....
첫번째 for문 안에 넣을 생각을 못했다,....
변수는 단순 선언 뿐 아니라 들어온 값들을 초기화 시킬수도 있기때문에
단순하게 생각하지말고, 어디서 어떤 값을 어떻게 넣고 초기화 시킬 것인지를 잘 생각해보자.
