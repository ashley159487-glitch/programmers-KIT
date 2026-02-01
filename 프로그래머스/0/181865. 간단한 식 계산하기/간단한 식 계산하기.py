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
        
        
    