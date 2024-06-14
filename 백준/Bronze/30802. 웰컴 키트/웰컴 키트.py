import sys
input=sys.stdin.readline

n=int(input())
shirts=list(map(int, input().rstrip().split()))
t,p=map(int, input().split())

packs=0
for shirt in shirts:
    if shirt%t!=0:
        packs+=shirt//t+1
    else:
        packs+=shirt//t

print(packs)
print(n//p, n%p, sep=' ')