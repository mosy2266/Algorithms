from collections import deque

def solution(begin, target, words):
    words = [begin] + words
    n = len(words)
    graph=[[] for _ in range (n)]
    visited=[False]*n
    dist=[1]*n
    
    if target not in words:
        return 0
    
    target_idx = words.index(target)

    for i in range(n-1):
        for j in range(i+1, n):
            dif_num = 0
            for k in range(len(begin)):
                if words[i][k] != words[j][k]: dif_num+=1
            if dif_num==1:
                graph[i].append(j)
                graph[j].append(i)
    
    def bfs(start):        
        q=deque([start])
        visited[start]=True
        
        while q:
            v=q.popleft()
            prev=v
            
            for e in graph[v]:
                if not visited[e]:
                    visited[e]=True
                    dist[e] += dist[prev]
                    q.append(e)
    
    bfs(0)
    return dist[target_idx]-1