from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    for i in answer :
        return i