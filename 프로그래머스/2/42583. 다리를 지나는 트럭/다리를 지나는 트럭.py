from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0]*bridge_length)
    queue = deque(truck_weights)
    bridge_weight = 0
    
    while bridge:
        answer+=1
        bridge_weight -= bridge.popleft()
        
        if queue:
            if bridge_weight + queue[0] <= weight:
                truck = queue.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)
        
    return answer