def solution(strArr):
    answer = []
    cnt = []
    for i in strArr :
        answer.append(len(i))
    for j in set(answer) :
        cnt.append(answer.count(j)) 여기까지 하면 cnt리스트 안에 answer리스트의 값들을 카운트 한 값이 들어가게 되고
    return max(cnt) 그 값들 중에서 가장 큰 값만 retunr한다.
=====================================
문제를 풀이 할 때는 바로 코드를 쓸 수 있을 줄 알았는데,
막상 풀다보니 각각 값의 길이를 리스트에 저장하고 나서 막혔었다...
문제를 보면 아 이렇게 하면 되겠다하고 머릿속에는 딱 떠오르는데
그걸 코드로 옮기는 게 쉽지가 않다.

일단 길이들을 구해서 리스트에 담은 다음 
다시 반복문으로 리스트에 있는 숫자들을 카운트 하는데 
숫자끼리 각각 카운트해서 가장 큰 값만 return하기.
