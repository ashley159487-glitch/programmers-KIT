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
==========================================================
정수를 문자열로 변환하는 것도 중요하지만 이 문제를 풀 수있는 핵심은
문자열로써는 비교할 수 없는(비교하기 애매한) 수들이 나왔을 때 그들을
어떻게 대소비교하냐이다.
일단 리스트 안의 정수들을 각각 문자열로 변환해서 리스트에 담은 후
정렬을 시켜주는데 여기서 코드를 보면 answer.sort(key = lambda x : x * 3, reverse = True) 이런 모습이다.
나는 lambda를 배우거나 써보지 않아서 얘기를 하자면 lambda는 임시로 쓰는 짧은 함수이다.

def 함수이름(x):
    return x * 3
이 식을 lambda를 이용하면 lambda x : x * 3
이렇게 되는 것이다.

그 후 sort로 정렬을 할 때도 내림차순으로 정렬해야하기 때문에 sort(key = ..., reverse = True)로 내림차순으로 바꿔준다.
그렇게되면 내림차순으로 리스트에 값들이 정렬되고 그 값들을 하나의 문자열로 합치면 정답이되는데 여기서 한가지 또 주의점이있다.
안의 값들이 다 0이라서 "000" 이런식으로 문자열은 합쳐버리기때문에
조건문으로 가장 큰 수가 0 이라면 "0"을 리턴시켜야 한다.
