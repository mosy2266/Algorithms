import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
ans=0

adj = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    u,v = map(int, input().split())

    adj[u-1].append(v)
    adj[v-1].append(u)

def dfs(graph, start, visited):
    global ans
    visited[start-1] = True
    for v in graph[start-1]:
        if visited[v-1] == False:
            ans+=1
            dfs(graph, v, visited)

dfs(adj, 1, visited)
print(ans)