import sys
from collections import deque

input=sys.stdin.readline

n,m = map(int, input().split())
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
    blocks=list(input().rstrip())
    graph.append(list(map(int, blocks)))

def bfs(a,b):
    queue = deque([(a,b)])

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

bfs(0,0)
print(graph[n-1][m-1])