from collections import deque

def solution(elements):
    n = len(elements)
    q = deque(elements)
    sums = set()
    
    for i in range(1,n+1):
        for j in range(n):
            num = sum(list(q)[:i])
            q.rotate(-1)
            sums.add(num)
            
    answer = len(sums)
    return answer