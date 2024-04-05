import sys
input=sys.stdin.readline

N=int(input())

for _ in range (N):
    PS=input().rstrip()
    if PS[0]=="(":
        while "()" in PS:
            PS=PS.replace("()","")
        if not PS:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")