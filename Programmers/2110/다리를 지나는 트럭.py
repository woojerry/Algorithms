from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0] * bridge_length) 
    truck_queue = deque(truck_weights)   
    bridge_weight = 0
    
    while queue:
        print(answer, truck_queue, bridge_weight)
        answer += 1
        bridge_weight -= queue.popleft()
        
        if truck_queue:
            if bridge_weight + truck_queue[0] <= weight:
                truck_weight = truck_queue.popleft()
                bridge_weight += truck_weight
                queue.append(truck_weight)
            else:
                queue.append(0)
                
    
    return answer

print(solution(2,10,[7,4,5,6]))