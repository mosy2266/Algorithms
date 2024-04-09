from collections import deque

N=int(input())
prcs=list(map(int, input().split()))
prcs=prcs[-1::-1]

answer=deque([])

k=1
while k<=N:
    for prc in prcs:
        if len(answer)<=1:
            if prc==1:
                answer.appendleft(k)
            else:
                answer.append(k)
            k+=1
        else:
            if prc==1:
                answer.appendleft(k)
            elif prc==2:
                answer.insert(1, k)
            else:
                answer.append(k)
            k+=1
print(*answer)