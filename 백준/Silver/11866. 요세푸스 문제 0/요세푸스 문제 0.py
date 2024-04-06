from collections import deque

N,K=map(int, input().split())
nums=deque([i for i in range(1,N+1)])

print("<", end="")
while nums:
    nums.rotate(-(K-1))
    print(nums.popleft(), end="")
    if len(nums)!=0:
        print(", ", end="")
print(">")