def solution(myString):
    answer = []
    for i in myString.split("x") :
        answer.append(len(i))
    return answer
=======================================
처음엔 split을 하고 각 문자열의 갯수를 어떻게 표현 할까를 고민했었다.
len() 을 쓰면 각 문자열의 길이만큼 갯수로 표현되므로
리스트 안에 수로 표현되는 걸 깨달았다.
        
    
        
            
        
        
    
    
