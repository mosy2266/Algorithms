from itertools import combinations

N,M=map(int, input().split())
cards=list(map(int, input().split()))
combs=list(combinations(cards, 3))
sums=set([sum(x) for x in combs if sum(x)<=M])

print(max(sums))