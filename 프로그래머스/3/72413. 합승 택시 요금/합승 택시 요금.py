import heapq

def solution(n, s, a, b, fares):
    
    graph = [[] for _ in range(n+1)]
    fee = [0]*(n+1)
    
    for x,y,w in fares:
        graph[x].append((y,w))
        graph[y].append((x,w))
    
    def dijk(start):
        q = []
        heapq.heappush(q, (start, 0))
        distance[start] = 0
        
        while q:
            now,dist = heapq.heappop(q)
            if distance[now] < dist: continue
            
            for k,w in graph[now]:
                cost = dist + w
                if cost < distance[k]:
                    distance[k] = cost
                    heapq.heappush(q, (k, cost))
    
    for i in [s,a,b]:
        distance = [float('inf')]*(n+1)
        dijk(i)
        
        for j in range(1, n+1):
            fee[j] += distance[j]
    
    return min(fee[1:])