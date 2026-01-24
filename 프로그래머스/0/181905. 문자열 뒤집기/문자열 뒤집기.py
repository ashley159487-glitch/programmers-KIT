def solution(my_string, s, e):
    sli = my_string[:s] + my_string[s:e + 1][::-1] + my_string[e + 1:]
    return sli

문제를 보고 무조건 for문이나 if문을 적는 버릇을 고치니까
오히려 좀 더 문제를 보는 시야가 넓어진 것 같다.
이 문제는 단순히 slicing을 해서 이어붙이면 되는 문제이기에
for문이나 if로 뭘 해보려 하지 않고 단순하게 잘라서 이어붙여보았다.
