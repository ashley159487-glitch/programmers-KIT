def solution(rank, attendance):
    places = []
    for i, j in enumerate(rank) :
        if attendance[i] :
            places.append((j, i))
    places = sorted(places)[:3]
    (_,a), (_,b), (_,c) = places
    return 10000 * a + 100 * b + c
======================================
이 문제는 등수를 직접 식에 대입하는게 아니라
그 등수들의 인덱스를 식에 대입해야 하므로
인덱스와 값을 true인 것만 동시에 뽑아와서 듀플형태로
리스트에 저장하고 등수별로 정렬시킨 뒤
언패킹으로 인덱스 값만 뽑아서 계산식에 대입시키면 풀린다.
