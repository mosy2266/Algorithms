import sys
input=sys.stdin.readline

n=int(input())
stairs=[0]

for i in range(n):
    stairs.append(int(input()))

if n==1:
    print(stairs[1])
elif n==2:
    print(stairs[1]+stairs[2])
else:
    dp=[0]*(n+1)
    dp[1]=stairs[1]
    dp[2]=stairs[1]+stairs[2]
    dp[3]=stairs[3]+max(stairs[1],stairs[2])
    for i in range(4,n+1):
        dp[i]=stairs[i]+max(dp[i-3]+stairs[i-1],dp[i-2])
    print(dp[n])