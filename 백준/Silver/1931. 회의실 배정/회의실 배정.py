import sys
input=sys.stdin.readline

N=int(input())
times=[]
for _ in range(N):
    times.append(list(map(int, input().rstrip().split())))

times.sort(key=lambda x: (x[1], x[0]))

i,j=0,1
cnt=1
while j<N:
    start=times[j][0]
    end=times[i][1]
    if end>start:
        j+=1
        continue
    else:
        i=j
        j+=1
        cnt+=1
        continue

print(cnt)