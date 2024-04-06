from collections import deque

N,K=map(int, input().split())
nums=deque([i for i in range(1,N+1)])
answer=[]

while nums:
    nums.rotate(-(K-1))
    answer.append(str(nums.popleft()))

print("<",", ".join(answer),">", sep="")    