import heapq, math

def solution(n, s, a, b, fares):
    INF = math.inf
    graph = [[] for _ in range(n+1)]
    
    points = [a,b,s]
    charge = [0]*(n+1)
    
    
    for x,y,w in fares:
        graph[x].append((y,w))
        graph[y].append((x,w))
    
    def dijk(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            if distance[now]<dist: continue
            
            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    for p in points:
        distance = [INF]*(n+1)
        dijk(p)
        
        for i in range(1,n+1):
            charge[i] += distance[i]
    
    return min(charge[1:])