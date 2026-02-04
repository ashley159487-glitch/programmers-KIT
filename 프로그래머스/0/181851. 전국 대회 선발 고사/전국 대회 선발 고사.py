def solution(rank, attendance):
    places = []
    for i, j in enumerate(rank) :
        if attendance[i] :
            places.append((j, i))
    places = sorted(places)[:3]
    (_,a), (_,b), (_,c) = places
    return 10000 * a + 100 * b + c