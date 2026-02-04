from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    for i in answer :
        return i
========================================================
Counter를 쓰면 변수 안의 값이 몇변 나왔는지 카운트해서 딕셔너리 형태로 만들어준다.
Counter객체끼리는 빼기가 가능하므로 빼면 마라톤을 완주하지 못한 한 사람의 이름만 남게되고,
그걸 반복문 돌리면 키값만 반환되므로 그걸 return하면 된다.
