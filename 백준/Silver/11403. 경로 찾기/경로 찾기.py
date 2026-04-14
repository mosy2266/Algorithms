import sys,math
input=sys.stdin.readline

INF=math.inf

n=int(input())
matrix=[]
graph=[[INF]*n for _ in range(n)]

for i in range(n):
    adj=list(map(int, input().split()))
    matrix.append(adj)

    for j in range(n):
        if adj[j]==1:
            graph[i][j]=1


for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            if graph[i][j]!=INF:
                matrix[i][j]=1

for m in matrix:
    print(*m)
