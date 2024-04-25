import sys
input=sys.stdin.readline

nums=[0]*11
nums[1]=1
nums[2]=2
nums[3]=4

for _ in range(int(input())):
    k=int(input())
    if k<=3:
        print(nums[k])
    else:
        for i in range(4, k+1):
            nums[i]=nums[i-1]+nums[i-2]+nums[i-3]
        print(nums[k])