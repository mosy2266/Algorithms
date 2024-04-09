from collections import deque

N=int(input())
prcs=list(map(int, input().split()))
r_prcs=prcs[-1::-1]
cards=[i for i in range(1,N+1)]

answer=deque([])

k=1
while k<=N:
    for prc in r_prcs:
        if len(answer)<=1:
            if prc==1:
                answer.appendleft(k)
            else:
                answer.append(k)
            k+=1
        else:
            if prc==1:
                answer.appendleft(k)
                k+=1
            elif prc==2:
                answer.insert(1, k)
                k+=1
            else:
                answer.append(k)
                k+=1
print(*answer)