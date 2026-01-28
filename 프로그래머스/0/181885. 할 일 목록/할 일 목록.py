def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)) :
        for j in range(len(finished)) :
            if i == j :
                if finished[j] == False :
                    answer.append(todo_list[i])
    return answer