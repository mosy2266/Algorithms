import heapq, math

def solution(n, s, a, b, fares):
    INF = math.inf
    answer = 0
    graph = [[] for _ in range(n+1)]
    charge = [0]*(n+1)
    order=[s,a,b]
    
    for fare in fares:
        x,y,w = fare
        graph[x].append((y,w))
        graph[y].append((x,w))
    
    def dijk(start):
        q = []
        heapq.heappush(q, (0, start))
        weight[start]=0
        
        while q:
            dist, now = heapq.heappop(q)
            if weight[now] < dist : continue
            for i in graph[now]:
                cost = dist + i[1]
                if weight[i[0]] > cost:
                    weight[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    for o in order:
        visited = [False]*(n+1)
        weight = [INF]*(n+1)

        dijk(o)

        for j in range(1, n+1):
            charge[j] += weight[j]
                
    return min(charge[1:])