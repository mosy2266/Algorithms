import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int, input().split()))
nums.sort()

ans=0
for i in range(n,0,-1):
    ans+=sum(nums[:i])

print(ans)