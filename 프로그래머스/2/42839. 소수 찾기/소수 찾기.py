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
    
    

     