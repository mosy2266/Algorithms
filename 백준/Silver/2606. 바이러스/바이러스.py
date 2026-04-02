import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
m=int(input())
adj=[[] for i in range(n)]
visited=[False]*n
queue=deque([])

for i in range(m):
    u,v=map(int, input().split())

    adj[u-1].append(v)
    adj[v-1].append(u)

def bfs(graph, start, visited, queue):
    ans=0
    visited[start-1] = True

    for i in graph[start-1]:
        queue.append(i)

    while queue:
        u = queue.popleft()
        visited[u-1] = True
        ans+=1
        for v in graph[u-1]:
            if visited[v-1] == False and v not in queue:
                queue.append(v)

    return ans

print(bfs(adj, 1, visited, queue))