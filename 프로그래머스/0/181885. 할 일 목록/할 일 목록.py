def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)) :
        for j in range(len(finished)) :
            if i == j :
                if finished[j] == False :
                    answer.append(todo_list[i])
    return answer

====================================================
통과는 했다. 근데 말 그대로 통과만 한 코드다.
이걸 좋아해야하나... 예전에는 통과는 커녕 코드를 쓰지도 못하고
제미나이한테 힌트를 물어보거나, 질문하기에 들어가서 다른 사람의 코드를 보며
따라쳤을 가능성이 농후했다.
그래도 이제 문제를 보고 코드를 칠 수는 있게됐다.
그래도 복기를 해보자면 이 문제는 굳이 2중for문을 돌릴 필요없이
def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if not finished[i]:
            answer.append(todo_list[i])
    return answer
이런 식으로 for문으로 뽑아낸 인덱스를 바로 finished의 인덱스와 비교가 가능했다.
나는 문제의 입출력 예를 보고 저게 그냥 문자열인줄 알고 2중 for문으로 풀었는데
문자열이어도 위의 코드로 풀 수 있는 문제였다.
인덱스 값의 일치를 생각 해두자.
