import sys
input=sys.stdin.readline

N=int(input())
nums=[int(input()) for _ in range(N)]
cnt={}
nums.sort()

if sum(nums)>=0:
    print(int(sum(nums)/N+0.5))
else:
    print(int(sum(nums)/N-0.5))
print(nums[(N-1)//2])

rg=nums[-1]-nums[0]

for num in nums:
    if num in cnt.keys():
        cnt[num]+=1
    else:
        cnt[num]=1

modes=list(cnt.values())

if modes.count(max(modes))>1:
    nums_cnt=[]
    for k,v in cnt.items():
        if v==max(modes):
            nums_cnt.append(k)
    print(nums_cnt[1])

else:
    for k,v in cnt.items():
        if v==max(modes):
            print(k)
            break

print(rg)