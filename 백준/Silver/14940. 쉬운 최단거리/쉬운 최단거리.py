import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int, input().split())
ground=[]
start=deque()

for i in range(n):
    ground.append(list(map(int, input().split())))
    for j in range(m):
        if ground[i][j]==2: #시작점 위치를 찾으면 덱에 삽입
            start.append([i,j])
            x,y=i,j

def bfs(a,b): #bfs 정의
    #거리 및 방문 여부 저장
    visited=[[-1 for _ in range(m)] for _ in range(n)]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visited[a][b]=0
    while start:
        x,y=start.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                #갈 수 있는 땅(ground=1)이면서 방문한 적 없으면(visited=-1)
                if ground[nx][ny]==1 and visited[nx][ny]==-1:
                    #해당 위치의 visited에 (이전 위치 visited)+1한 값을 저장
                    visited[nx][ny] = visited[x][y]+1
                    start.append([nx,ny])
    return visited

ans=bfs(x,y)

for i in range(n):
    for j in range(m):
        if ground[i][j]==0:
            print(0, end=' ')
        else:
            print(ans[i][j], end=' ')
    print()