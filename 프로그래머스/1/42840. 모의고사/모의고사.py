def solution(answers):
    answer = []
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    std1Score = 0
    std2Score = 0
    std3Score = 0
    for i, j in enumerate(answers) :
        if j == std1[i % len(std1)] :
            std1Score += 1
        if j == std2[i % len(std2)] :
            std2Score += 1
        if j == std3[i % len(std3)] :
            std3Score += 1
    maxScore = max(std1Score, std2Score, std3Score)
    if maxScore == std1Score :
        answer.append(1)
    if maxScore == std2Score :
        answer.append(2)
    if maxScore == std3Score :
        answer.append(3)
    return answer