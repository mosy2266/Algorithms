import sys
input=sys.stdin.readline

n, m = list(map(int, input().split()))
nums=[]

def dfs(start):
    if len(nums)==m:
        print(' '.join(map(str,nums)))
        return
    
    for i in range(start, n+1):
        if i not in nums:
            nums.append(i)
            dfs(i+1)
            nums.pop()

dfs(1)