from collections import deque

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False]*n
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 and i!=j:
                graph[i].append(j)
    
    def bfs(start):
        q = deque([start])
        
        while q:
            v = q.popleft()
            visited[v]=True
            
            for n in graph[v]:
                if not visited[n]:
                    visited[n]=True
                    q.append(n)

    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer+=1
    
    return answer