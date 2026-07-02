import math, heapq

def solution(n, s, a, b, fares):
    INF = math.inf
    graph = [[] for _ in range(n+1)]
    charge = [0]*(n+1)
    
    for x,y,w in fares:
        graph[x].append((y,w))
        graph[y].append((x,w))
    
    def dijk(start):
        q = []
        heapq.heappush(q, (start, 0))
        distance[start] = 0
        
        while q:
            now, dist = heapq.heappop(q)
            if dist > distance[now]: continue
            for v in graph[now]:
                cost = dist + v[1]
                if distance[v[0]] > cost:
                    distance[v[0]] = cost
                    heapq.heappush(q, (v[0], cost))
    
    for i in [s,a,b]:
        distance = [INF]*(n+1)
        dijk(i)
        
        for j in range(1, n+1):
            charge[j] += distance[j]
    
    return min(charge[1:])