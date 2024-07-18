from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int, input().split())
campus=[]
start=deque()

for i in range(n):
    info=list(input().rstrip())
    if 'I' in info:
        x,y=info.index('I'),i
        start.append([x,y])
    campus.append(info)

def bfs(a,b):
    cnt=0
    visited=[[-1 for _ in range(m)] for _ in range(n)]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visited[b][a]=0

    while start:
        x,y=start.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if campus[ny][nx]!='X' and visited[ny][nx]==-1:
                    if campus[ny][nx]=='P':
                        cnt+=1
                    visited[ny][nx]=1
                    start.append([nx,ny])
    return cnt

ans=bfs(x,y)
if ans!=0:
    print(ans)
else:
    print("TT")