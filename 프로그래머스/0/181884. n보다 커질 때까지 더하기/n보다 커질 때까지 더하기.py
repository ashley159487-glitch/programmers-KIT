def solution(numbers, n):
    answer = 0
    for i in numbers :
        answer += i
        if answer > n :
            return answer
=============================
이 문제는 인덱스를 구할 필요가 없으므로
numbers의 값들을 직접 뽑아 내 answer변수에 +=를 한 후,
if문으로 n보다 클 때 바로 return시키면 된다.

슬슬 문제를 보면 코드들이 머릿속에 그려지기 시작한다.
이 문제가 쉬워서겠지만 그래도 뿌듯하다.
