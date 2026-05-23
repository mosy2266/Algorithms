from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque([])
    
    for idx, p in enumerate(priorities):
        queue.append([p, idx])
        
    order=[]
    while queue:
        highest = max(queue)[0]
        priority, idx = queue.popleft()
        if priority >= highest:
            order.append(idx)
        else:
            queue.append([priority, idx])
    
    answer = order.index(location) + 1
    
    return answer
