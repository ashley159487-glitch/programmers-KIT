import math
def solution(progresses, speeds):
    answer = []
    for i, j in enumerate(progresses) :
        days = math.ceil((100 - j) / speeds[i])
        answer.append(days)
    target_day = answer[0]
    count = 1
    final = []
    for i in range(1, len(answer)) :
        if target_day >= answer[i] :
            count += 1
        else :
            final.append(count)
            count = 1
            target_day = answer[i]
    final.append(count)
    return final

# 각 기능별로 완성되기까지 남은 날짜 구하고 순서대로 리스트에 넣기
# 첫번째 기능이 끝나는 날짜를 기준일로 잡고 그 다음 기능들의 날짜와 비교하기
# 뒷사람 날짜 <= 기준일 = 같이 배포
# 뒷사람 날짜 > 기준일 배포를 끊고 뒷사람을 기준일로 삼기
============================================================================
레벨이 높아질수록 수학적 사고를 요구하는 문제가 많아지네 일단 여기서 내가 느낀 나의 문제점들을 나열해보면
1. 각 작업이 완료될 날짜를 구할 줄 모름(수학적 사고x)
2. math함수를 쓰거나 안 쓰더라도 실수을 올림해 정수로 만들 줄 모름(도구의 활용x)
3. 아직도 원하는 값을 찾은 후 그것을 바로 이용해야 할 지 변수에 넣어서 이용해야 할 지 감을 못 잡음.
4. 반복문으로 돌릴 때 직접 그 값을 꺼내야 할 지, 인덱스로 값을 출력해야 할 지 감을 못 잡음.
5. 가장 근본적인 문제는 문제를 읽고 그걸 어떻게 코드로 구현해야 할까 고민하고 글로 옮겨야 하는데 그것조차 못함
==============================================================================================================
def solution(progresses, speeds):
    answer = []
    for i, j in enumerate(progresses) :
        days = (100 - j + speeds[i] - 1) // speeds[i]
        answer.append(days)
    target = answer[0]
    total = []
    cnt = 1
    for i in range(1, len(answer)) :
        if answer[i] <= target :
            cnt += 1
        else :
            total.append(cnt)
            cnt = 1
            target = answer[i]
    total.append(cnt)
    return total
======================================================================
math함수를 쓰지 않고 수학식과 몫연산자를 활용한 풀이식.
