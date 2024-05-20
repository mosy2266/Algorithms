import sys
input=sys.stdin.readline
from collections import deque

m,n=map(int, input().split())
box=[]
green=0
red=deque()
ans=0

for i in range(n):
    box.append(list(map(int, input().rstrip().split())))
    for j in range(m):
        if box[i][j]==1:
            red.append([i,j,1])
        elif box[i][j]==0:
            green+=1

while green>0 and len(red)>0:
    x,y,ans=red.popleft()

    if x>0:
        if box[x-1][y]==0:
            box[x-1][y]=1
            red.append([x-1,y,ans+1])
            green-=1
    if x<n-1:
        if box[x+1][y]==0:
            box[x+1][y]=1
            red.append([x+1,y,ans+1])
            green-=1
    if y>0:
        if box[x][y-1]==0:
            box[x][y-1]=1
            red.append([x,y-1,ans+1])
            green-=1
    if y<m-1:
        if box[x][y+1]==0:
            box[x][y+1]=1
            red.append([x,y+1,ans+1])
            green-=1

if green==0:
    print(ans)
else:
    print(-1)