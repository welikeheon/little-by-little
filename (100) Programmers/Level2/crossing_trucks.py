from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    curr_weight = 0
    while truck_weights:
        answer += 1
        curr_weight -= bridge.popleft()
        if curr_weight+truck_weights[0] <= weight:
            curr_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    while bridge:
        answer += 1
        bridge.popleft()
    
    return answer
