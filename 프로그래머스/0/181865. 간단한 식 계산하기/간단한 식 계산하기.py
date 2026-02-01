def solution(binomial):
    parts = binomial.split()
    a = int(parts[0])
    b = int(parts[2])
    op = parts[1]
    if op == "+" :
        return a + b
    elif op == "-" :
        return a - b
    else :
        return a * b
=====================================
각 공백을 기준으로 split까지는 생각을 했는데
각각 나눠진 값들이 문자열이므로 그걸 어떻게 계산을 시킬까를 고민했다.
변수의 선언이 어느 문제든 중요한 거같다.
변수를 만들어주면 위의 코드처럼 해결이 되는데 이걸 반복문으로 빼내서 해결하려고 하니
생각이 머릿속에서 엉켰었다.
언패킹을 하면 더 짧게 쓸 수 있다.
a, b, op = binomial.split()
이렇게 언패킹 후 계산 할 때만 a, b를 형변환 시켜서
조건문으로 계산시키면 된다.
        
        
    
