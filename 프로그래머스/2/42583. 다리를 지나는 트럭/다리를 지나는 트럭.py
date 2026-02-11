def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge = [0] * bridge_length
    bridge_weight = 0
     
    while bridge :
        cnt += 1
        bridge_weight -= bridge.pop(0)
        if truck_weights :
            if weight >= truck_weights[0] + bridge_weight :
                truck = truck_weights.pop(0)
                bridge.append(truck)
                bridge_weight += truck
            else :
                bridge.append(0)
    return cnt

#반복문 안에 cnt += 1을 집어넣어 마지막 차가 완전히 빠져나갈 때 cnt 리턴시키기
