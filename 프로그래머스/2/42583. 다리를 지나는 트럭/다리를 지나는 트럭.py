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
================================================================
초를 세줄 cnt변수, 다리 길이를 시각화 해 줄 bridge변수, 현재 다리무게의 변수를 각각 만들고 while문을 돌려준다.
반복문의 길이는 시각화 해놓은 bridge변수만큼 잡아주고, 조건문을 잡아주는데 pop으로 트럭무게리스트에서 값들을 빼내면
리스트가 점점 짧아져 결국 0이되면 에러가 나므로 조건문으로 리스트에 값이 들어있을 때만 반복문이 돌게 한다.
그 후 현재다리위의 무게 + 첫번째 트럭의 무게가 다리가 버틸수있는 무게 이하일 때 트럭 리스트에서 트럭을 빼내 bridge변수에 집어넣는다.
그 후 다리의 현재무게에도 트럭의 무게를 더해준다. 그 후 else로 반대의 경우 다리 리스트에 0을 넣어주면 총 시각이 카운트 되어 리턴된다.
여기서 주의 할 것은 bridge_weight -= bridge.pop(0) 이 식으로 계속해서 리스트의 맨 앞의 값을 없애줘야 한다는 것이다.
