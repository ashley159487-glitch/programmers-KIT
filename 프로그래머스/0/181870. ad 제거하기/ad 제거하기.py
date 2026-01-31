def solution(strArr):
    answer = []
    for i in strArr :
        if "ad" not in i :
            answer.append(i)
    return answer
================================
복잡하게 2중for문으로 돌려가면서 지울 필요 없이
not in으로 걸러내면 된다.
이 때 not과 in의 위치를 다르게 하면 결과값도 달라지니
위치에 주의하도록 하자.
