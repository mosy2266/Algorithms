import sys
input=sys.stdin.readline

for i in range(1, int(input())+1):
    sen=input().rstrip()
    print(i,". ",sen, sep='')