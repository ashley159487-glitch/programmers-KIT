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
=========================================
이 문제는 각 인덱스 별로 [이름, 종류] 이렇게 값이 들어가있다.
그러므로 반복문으로 언패킹 후 종류들만 리스트에담은 후
collections 라이브러리를 import 한 다음
그 안에 Counter기능으로 리스트를 딕셔너리형태로 (ex) { 종류 : 갯수 }) 만든다.
딕셔너리로 만들었으면 그 딕셔너리를 반복문으로 돌려서 갯수들만 빼낸 후
각 종류에 + 1 을 한 후 곱해준다.
여기서 왜 각 종류에 + 1을 한 후 곱해줘야하나?
예를들어 얼굴 부위에 [안경, 선글라스] 이렇게 두가지가 있다면 선택 할 수 있는 종류는
안경, 선글라스, 안입기 이렇게 3가지가 된다. 안입기는 모든 옷 종류에 하나씩 넣어야 하므로  + 1을 해준다.
이렇게 모든 종류에 + 1을 해준 후 이 숫자들을 모두 곱하면 모든 조합의 수가 나오는데
여기서 주의해야 할 점은 "코니는 하루에 최소 한 개의 의상은 입습니다." 이것이다.
그러므로 모든 의상을 안 입는 방법을 -1 해줘야 하므로 구한 수에 - 1을 해주면
결과값이 나온다.
==========================================
def solution(clothes):
    answer = 1
    kinds = []
    for i, j in clothes :
        kinds.append(j)
    counts = {}
    for i in kinds :
        counts[i] = counts.get(i, 0) + 1
    for i in counts.values() :
        answer *= i + 1
    return answer - 1
===========================================
이번 풀이는 collections 라이브러리를 사용하지 않고
반복문으로 직접 리스트에서 딕셔너리로 변환시킨 후
값들을 계산후 답을 도출하는 풀이이다.
counts[i] = counts.get(i, 0) + 1의 의미는 "있으면 있는 거에 1 더하고, 없으면 0에서 1 더해라."라는 뜻이다.
