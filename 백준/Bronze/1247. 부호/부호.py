import sys
input=sys.stdin.readline

for _ in range(3):
    S=0
    for i in range(int(input())):
        S+=int(input())
    if S==0:
        print(0)
    elif S>0:
        print('+')
    else:
        print('-')