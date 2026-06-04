from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n)]
    dist = [1]*n
    visited=[False]*n
    
    for e in edge:
        graph[e[0]-1].append(e[1]-1)
        graph[e[1]-1].append(e[0]-1)
        
    def bfs(start):
        q=deque([start])
        visited[start]=True
        
        while q:
            v=q.popleft()
            prev=v
            for n in graph[v]:
                if not visited[n]:
                    dist[n] += dist[prev]
                    visited[n]=True
                    q.append(n)
    
    bfs(0)
    dist.sort(reverse=True)
    
    return dist.count(dist[0])