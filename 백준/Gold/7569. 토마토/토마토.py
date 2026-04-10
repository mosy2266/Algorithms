import sys, math
from collections import deque

input = sys.stdin.readline

m,n,h = map(int, input().split())
tomatoes=[[] for _ in range(h)]
red_tomato=deque()
green=0

for i in range(h):
    for j in range(n):
        tomato=list(map(int, input().split()))
        tomatoes[i].append(tomato)
        green+=tomato.count(0)
        for k in range(m):
            if tomato[k]==1:
                red_tomato.append((i,j,k))

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

def bfs(queue, green):
    days=-math.inf
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx,ny,nz = x+dx[i], y+dy[i], z+dz[i]

            if 0<=nx<n and 0<=ny<m and 0<=nz<h and tomatoes[nz][nx][ny]==0:
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                if tomatoes[nz][nx][ny] > days:
                    days = tomatoes[nz][nx][ny]
                green-=1
                queue.append((nz,nx,ny))
            
    return days-1, green

ans, remain_green = bfs(red_tomato, green)

if green==0:
    print(0)
elif remain_green > 0:
    print(-1)
else:
    print(ans)