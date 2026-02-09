import collections
def solution(clothes):
    answer = 1
    kind = []
    for i, j in clothes :
        kind.append(j)
    counts = collections.Counter(kind)
    for i in counts.values() :
        answer *= i + 1
    return answer - 1