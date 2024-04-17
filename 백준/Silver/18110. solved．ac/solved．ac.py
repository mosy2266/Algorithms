from collections import deque
import sys
input=sys.stdin.readline

n=int(input())

if n==0:
    print(0)

else:
    dif=[int(input()) for _ in range(n)]
    dif.sort()
    q=deque(dif)

    if len(q)*0.15>=0.5:
        if (len(q)*0.15)%0.5==0:
            exclude=int(len(q)*0.15+0.5)
        else:
            exclude=round(len(q)*0.15)
        for _ in range(exclude):
            q.pop()
            q.popleft()
    
    if (sum(q)/len(q))%0.5==0:
        ans=int(sum(q)/len(q)+0.5)
    else:
        ans=round(sum(q)/len(q))
    print(ans)