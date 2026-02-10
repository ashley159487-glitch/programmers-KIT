from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    for i in answer :
        return i
========================================================
Counter를 쓰면 변수 안의 값이 몇변 나왔는지 카운트해서 딕셔너리 형태로 만들어준다.
Counter객체끼리는 빼기가 가능하므로 빼면 마라톤을 완주하지 못한 한 사람의 이름만 남게되고,
그걸 반복문 돌리면 키값만 반환되므로 그걸 return하면 된다.
========================================================
collection 라이브러리를 쓰지 않고 반복문으로 딕셔너리를 만들어 활용하는 방법에 대해 알아보았다.

def solution(participant, completion):
    answer = {}
    for i in participant :
        answer[i] = answer.get(i, 0) + 1
    for i in completion :
        answer[i] -= 1
    for i in answer :
        if answer[i] > 0 :
            return i

첫번째 반복문에서 participant 리스트 안의 값들을 딕셔너리 형태로 만들어
키 : 밸류 로 저장시킨다. 여기서 키는 선수 이름 밸류는 선수이름의 갯수이다.
그다음 반복문으로 딕셔너리 안에 completion 리스트에 있는 선수들의 이름이 있으면
밸류를 -1시킨다.
그 다음 반복문으로 딕셔너리의 밸류값이 0보다 큰 키값만 return시킨다.
