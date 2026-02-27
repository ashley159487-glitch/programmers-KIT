def solution(numbers, target):
    answer = 0
    def dfs(index, current) :
        nonlocal answer
        if index == len(numbers) :
            if current == target :
                answer += 1
            return
        dfs(index + 1, current + numbers[index])
        dfs(index + 1, current - numbers[index])
    dfs(0, 0)
    return answer
===================================================
dfs(index + 1, current + numbers[index]) 이 코드에서 numbers의 모든 수를 더하게 된다
그 값이 target과 같으면 return하고 아니면 안가본 코드 dfs(index + 1, current - numbers[index])
에 들어간다.
    
모든 dfs 문제는 이 구조를 벗어나지 않는다.
1. 내가 설정한 끝에서 목표가 달성되었는지 확인 후 달성했으면 return 아니면 복귀.
2. 갈림길개수마다 코드만들기(갈림길이 2개면 코드 2개, 만약 많다면 반복문으로)
3. 출발점 정해주기
