def solution(my_string, index_list):
    answer = ''
    for i in index_list :
        answer += my_string[i]
    return answer

분명 몇 번 풀었던 유형의 문제였는데...
성장을 못하냐 왜...
index_list에서 숫자를 하나씩 꺼내기
-> 그 숫자를 인덱스 삼아 my_string[i]로 글자 뽑기
-> answer에 +=하기...
문자열 만드는 건 +=가 필수다

무엇을 반복시켜야 하는지 잘 생각하자.
