import sys
input=sys.stdin.readline

a,b,c=1,2,3
for _ in range(int(input())):
    x,y=map(int, input().split())
    if (x==a and y==b) or (x==b and y==a):
        a,b=b,a
    elif (x==a and y==c) or (x==c and y==a):
        a,c=c,a
    elif (x==b and y==c) or (x==c and y==b):
        b,c=c,b
print(a)