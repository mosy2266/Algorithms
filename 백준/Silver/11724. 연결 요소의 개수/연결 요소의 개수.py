import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int, input().split())
adj=[[] for _ in range (n+1)]
visited=[False]*(n+1)

for _ in range(m):
    u,v=map(int, input().split())

    adj[u].append(v)
    adj[v].append(u)

def dfs(graph,v,visited):
    visited[v]=True

    for i in graph[v]:
        if not visited[i]:
           dfs(graph,i,visited)
        
cnt=0
for i in range(1,n+1):
    if visited[i]==False:
        dfs(adj,i,visited)
        cnt+=1

print(cnt)