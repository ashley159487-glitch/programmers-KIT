def solution(picture, k):
    answer = []
    for i in picture :
        first = ""
        for j in i :
            first += j * k
        for e in range(k) :
            answer.append(first)
    return answer