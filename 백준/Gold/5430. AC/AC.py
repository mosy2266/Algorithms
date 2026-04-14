import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    p=input().rstrip()
    p.replace("RR", "")
    n=int(input())
    nums=deque(input().strip('[]\n').split(","))
    
    if n==0:
        nums.clear()

    success=True
    cnt=0
    for f in p:
        if f=="R":
            cnt+=1
        else:
            if not nums:
                print("error")
                success=False
                break
            else:
                if cnt%2==0:
                    nums.popleft()
                else:
                    nums.pop()
        
    if cnt%2!=0:
        nums.reverse()
    
    if success:
        print("[",",".join(nums),"]", sep="")