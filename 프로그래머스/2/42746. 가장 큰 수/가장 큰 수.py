def solution(numbers):
    answer = []
    last = ''
    for i in numbers :
        answer.append(str(i))
    answer.sort(key = lambda x : x * 3, reverse = True)
    for i in answer :   
        last += i
    if answer[0] == "0" :
        return "0"
    return last
