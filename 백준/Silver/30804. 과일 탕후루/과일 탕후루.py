n=int(input())
tanghulu=list(map(int, input().split()))
fruits=[0]*10

start,end,kind,ans=0,0,0,0

while end<n:
    fruits[tanghulu[end]]+=1
    if fruits[tanghulu[end]]==1:
        kind+=1

    if kind>2:
        fruits[tanghulu[start]]-=1
        if fruits[tanghulu[start]]==0:
            kind-=1
        start+=1
    ans=max(ans, end-start+1)
    end+=1

print(ans) 