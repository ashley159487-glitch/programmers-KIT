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