from itertools import combinations
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    fashion=dict()
    n=int(input())
    for _ in range(n):
        item,category=input().rstrip().split()
        if category not in fashion.keys():
            fashion[category]=1
        else:
            fashion[category]+=1
    
    ans=1
    for value in fashion.values():
        ans*=value+1
    print(ans-1)