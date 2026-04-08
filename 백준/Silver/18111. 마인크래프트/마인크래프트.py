import sys, math
input=sys.stdin.readline
INF=math.inf

n,m,b=map(int, input().split())
ground=[list(map(int, input().split())) for _ in range(n)]

min_time=INF
max_height=-INF

for h in range (257):
    used_block=0
    broken_block=0
    for i in range(n):
        for j in range(m):
            if (ground[i][j] > h):
                broken_block += ground[i][j] - h
            else:
                used_block += h - ground[i][j]

    if broken_block + b >= used_block:
        time = broken_block*2 + used_block
        if time <= min_time:
            min_time=time
            max_height=h

print(min_time, max_height)
