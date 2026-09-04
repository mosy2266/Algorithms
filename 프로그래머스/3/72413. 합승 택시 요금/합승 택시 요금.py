import math, heapq

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    charge = [0] * (n+1)
    
    for x,y,w in fares:
        graph[x].append((y,w))
        graph[y].append((x,w))
        
    def dijk(start):
        q = []
        heapq.heappush(q, (start, 0))
        distance[start] = 0
        
        while q:
            now, dist = heapq.heappop(q)
            if distance[now] < dist: continue
            
            for v in graph[now]:
                cost = dist + v[1]
                if cost < distance[v[0]]:
                    distance[v[0]] = cost
                    heapq.heappush(q, (v[0], cost))
    
    for i in [s,a,b]:
        distance = [math.inf] * (n+1)
        dijk(i)
        
        for j in range (1, n+1):
            charge[j] += distance[j]
    
    return min(charge[1:])