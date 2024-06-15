import sys
input=sys.stdin.readline

n,m=map(int, input().split())
sites=dict()

for _ in range(n):
    url,pw=input().rstrip().split()
    sites[url]=pw

for _ in range(m):
    print(sites[input().rstrip()])