from collections import deque

def solution(prices):
    answer = []
    
    queue = deque(prices)
    
    while queue:
        period = 0
        price = queue.popleft()
    
        if not queue:
            answer.append(period)
            break
        
        for p in queue:
            period+=1
            if price > p: break
        
        answer.append(period)
    
    return answer