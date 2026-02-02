import re
def solution(myStr):
    answer = []
    for i in re.split(r'[abc]', myStr) :
        if i != "" :
            answer.append(i)
    return answer if answer else ["EMPTY"]