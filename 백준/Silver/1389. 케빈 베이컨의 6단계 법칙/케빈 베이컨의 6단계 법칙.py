import sys
input=sys.stdin.readline

n,m=map(int, input().split())
INF=int(1e9)

table=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    table[i][i]=0

for _ in range(m):
    a,b=map(int, input().split())
    table[a][b]=1
    table[b][a]=1

for m in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            table[s][e]=min(table[s][e], table[s][m]+table[m][e])

ans=[INF]
for i in range(1,n+1):
    ans.append(sum(table[i][1:]))

print(ans.index(min(ans)))