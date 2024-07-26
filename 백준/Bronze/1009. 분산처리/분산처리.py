import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a,b=map(int, input().rstrip().split())
    end=str(a)[-1]
    if end=='1' or end=='5' or end=='6':
        print(end)
    elif end=='0':
        print(10)
    elif end=='4':
        if b%2==0:
            print(6)
        else:
            print(4)
    elif end=='9':
        if b%2==0:
            print(1)
        else:
            print(9)
    else:
        if b%4!=0:
            print(str(a**(b%4))[-1])
        else:
            print(str(a**4)[-1])