import sys
input=sys.stdin.readline

n,m=map(int, input().split())

pocketmons_num={}
pocketmons_name={}
for i in range(1,n+1):
    pocketmon=input().rstrip()
    pocketmons_num[i]=pocketmon
    pocketmons_name[pocketmon]=i

for _ in range(m):
    prob=input().rstrip()
    if prob.isalpha():
        print(pocketmons_name.get(prob))       
    else:
        print(pocketmons_num.get(int(prob)))