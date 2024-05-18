from collections import deque

n,k=map(int, input().split())
nums=[0]*100001

queue=deque([n])

while queue:
    temp=queue.popleft()
    if temp==k:
        print(nums[temp])
        break
    for i in (temp-1, temp+1, temp*2):
        if 0<=i<=100000 and nums[i]==0:
            nums[i]=nums[temp]+1
            queue.append(i)