import math, heapq

def solution(N, road, K):
    answer = 0
    INF = math.inf
    distance = [INF]*(N+1)
    graph = [[] for _ in range(N+1)]
    
    for x,y,w in road:
        graph[x].append((y,w))
        graph[y].append((x,w))
    
    def dijk(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        
        while q:
            dist, v = heapq.heappop(q)
            if distance[v] < dist: continue
            
            for i in graph[v]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    dijk(1)
    for i in distance[1:]:
        if i<=K: answer+=1
        
    return answer