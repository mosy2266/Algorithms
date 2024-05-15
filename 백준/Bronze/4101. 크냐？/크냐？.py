import sys
input=sys.stdin.readline

while True:
    a,b=map(int, input().rstrip().split())
    if a+b==0:
        break
    elif a>b:
        print("Yes")
    else:
        print("No")