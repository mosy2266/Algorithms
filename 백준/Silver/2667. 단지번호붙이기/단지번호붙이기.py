import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
apartments=[]
location=set()
ans=[]

for i in range(n):
    aparts=list(input().rstrip())
    apartments.append(list(map(int, aparts)))
    for j in range(n):
        if aparts[j]=='1':
            location.add((i,j))

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs():
    x,y=location.pop()
    apartments[x][y]=0
    apart_cnt=1

    queue=deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n and apartments[nx][ny]:
                apartments[nx][ny]=0
                apart_cnt+=1
                location.remove((nx,ny))
                queue.append((nx,ny))
    
    return apart_cnt

cnt=0
while location:
    ans.append(bfs())
    cnt+=1

print(cnt)
ans.sort()
for i in ans:
    print(i, end="\n")