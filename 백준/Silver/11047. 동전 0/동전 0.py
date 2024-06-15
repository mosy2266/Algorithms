import sys
input=sys.stdin.readline

n,k=map(int, input().split())
coins=[]

for _ in range(n):
    coins.append(int(input()))

ans=0
while k>0:
    coin=coins.pop()
    if k>=coin:
        ans+=k//coin
        k-=(k//coin)*coin

print(ans)