import heapq
import math

def solution(n, edge):    
    INF = math.inf
    graph = [[] for _ in range(n)]
    
    distance = [INF]*n
    visited=[False]*n
    
    for e in edge:
        graph[e[0]-1].append(e[1]-1)
        graph[e[1]-1].append(e[0]-1)
    
    def dijk(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start]=0
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distance[now] < dist : continue
            
            for i in graph[now]:
                if dist+1 < distance[i]:
                    distance[i] = dist+1
                    heapq.heappush(q, (dist+1, i))
    dijk(0)
    
    return distance.count(max(distance))