import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int, input().split()))
nums_set=set(nums)
x=int(input())
ans=0

for num in nums:
    if x-num in nums_set:
        ans+=1

print(ans//2)