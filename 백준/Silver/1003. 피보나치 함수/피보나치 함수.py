import sys
input=sys.stdin.readline

t=int(input())

def fibonacci(x):
    zero=[0]*41
    one=[0]*41
    zero[0]=one[1]=1
    zero[1]=one[0]=0

    if x>=2:
        for i in range(2,x+1):
            zero[i]=zero[i-1]+zero[i-2]
            one[i]=one[i-1]+one[i-2]
    
    return zero[x],one[x]

for _ in range(t):
    print(*fibonacci(int(input())))