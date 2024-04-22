import sys
input=sys.stdin.readline

n,m=map(int, input().split())

not_heard=set([input().rstrip() for _ in range(n)])
ans=[]
cnt=0
for _ in range(m):
    not_seen=input().rstrip()
    if not_seen in not_heard:
        cnt+=1
        ans.append(not_seen)

ans.sort()
print(cnt)
for x in ans:
    print(x)