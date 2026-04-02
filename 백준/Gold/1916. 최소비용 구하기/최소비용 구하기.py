import sys, math, heapq
INF = math.inf
input=sys.stdin.readline

n=int(input())
m=int(input())

graph=[[] for _ in range(n)]
weight=[INF]*n

for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u-1].append((v,w))

a,b = map(int, input().split())

def dijk(start):
    q=[]
    heapq.heappush(q, (0, start))
    weight[start-1]=0

    while q:
        w, now = heapq.heappop(q)

        if weight[now-1] < w: continue

        for i in graph[now-1]:
            cost = w + i[1]
            if cost < weight[i[0]-1]:
                weight[i[0]-1] = cost
                heapq.heappush(q, (cost, i[0]))

dijk(a)
print(weight[b-1])