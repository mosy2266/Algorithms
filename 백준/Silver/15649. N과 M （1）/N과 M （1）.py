import sys
input=sys.stdin.readline

n,m=map(int, input().split())
ans=[]

def backtrack():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(1,n+1):
        if i not in ans:
            ans.append(i)
            backtrack()
            ans.pop()

backtrack()