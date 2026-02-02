def solution(arr, flag):
    answer = []
    for i, j in enumerate(flag) :
        if j :
            answer += [arr[i]] * (arr[i] * 2)
        else :
            answer = answer[:-arr[i]]
    return answer
===============================================
리스트에는 -=가 없다.
마지막 원소를 제거하려면 슬라이싱으로 자르는 것이 편하다. pop() 도 있다.
리스트에 무언가를 추가하려면 append도 있지만
+= 도 있다 +=를 사용 할 땐 [arr[i]] * (arr[i] * 2) 이거처럼 형식을 잘 써야한다.
arr[i] * 2 이렇게 쓰면 에러난다.
