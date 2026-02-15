from itertools import permutations             
def solution(numbers):
    cnt = 0
    num_list = list(numbers)
    answer = set()
    for i in range(1, len(num_list) + 1) :
        for p in permutations(num_list, i) :
            answer.add(int("".join(p)))
    for i in answer :
        if is_prime(i) :
            cnt += 1
    return cnt
def is_prime(n) :
        if n < 2 :
            return False
        for i in range(2, n) :
            if n % i == 0 :
                return False
        return True
=====================================================
itertools안에 있는 permutations(순열)의 기능으로 어떤 리스트 안의 내용물을 순서를 따져서 줄을 세워준다.
이 때 반복시킬 범위를 잘 잡아주는 것이 중요하다. 1장부터 그 리스트의 최대길이까지 다 잡아줘야 하기 때문에
(1, len(num_list) + 1) 이렇게 범위를 잡아 준 후 위의 순열을 만들어주고, 그 값들을 만들어둔 변수에 담아주는데
각각의 값들은 튜플형식으로 되어있기 때문에 ex) ('1'), ('7'), ('1', '7'), ('7', '1') 떨어져 있는 값들을 합쳐주고
ex) ('1'), ('7'), ('17'), ('71') 정수로 바꿔줘서 변수에 넣어준다. 이 때 변수는 set() 으로 감싸져있어 중복 값들을 다 제거해줘야
나중에 소수를 카운트 할 때 오답이 안나온다.
여기까지 했으면 이제 소수인지를 판별해야 하는데 가독성을 위해 소수 판별 만 하는 함수를 하나 더 만들어준다.
소수란 1보다 큰 자연수 중에서 1과 자기 자신만을 약수로 가지는 수이기 때문에 0과 1을 빼주고 나머지를 반복문으로 돌려준다.
n % i == 0 의 뜻은 n을 i로 나눴을 때 나머지가 0인 지 묻는 것이고, 만약 맞다면 소수가 아니기 때문에 False를 이 반복문을
통과한 나머지는 True로 해주는 함수를 만든다.
그 후 solution함수에 is_prime함수를 대입해서 맞으면 카운트를 올려주는 반복문을 만들고 그 카운트를 리턴해주면 된다.
    
    

     
