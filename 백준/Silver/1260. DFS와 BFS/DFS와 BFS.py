import sys
input=sys.stdin.readline
from collections import deque

n,m,v=map(int, input().split())
adj=[[] for i in range (n+1)]
dfs_visited=[False]*(n+1)
bfs_visited=[False]*(n+1)

for _ in range(m):
    x,y=map(int, input().split())

    adj[x].append(y)
    adj[y].append(x)

for i in range(n+1):
    adj[i].sort()

def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, v, visited):
    queue=deque([v])
    visited[v]=True

    while queue:
        k=queue.popleft()
        print(k, end=" ")
        for i in graph[k]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

dfs(adj, v, dfs_visited)
print("")
bfs(adj, v, bfs_visited)