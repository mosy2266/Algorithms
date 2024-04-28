import sys
input=sys.stdin.readline

n,m=map(int, input().split())
nums=list(map(int, input().split()))
sums_nums=[0]
total=0
for num in nums:
    total+=num
    sums_nums.append(total)

for _ in range(m):
    i,j=map(int, input().split())
    print(sums_nums[j]-sums_nums[i-1])