day=int(input())
cars=list(map(int, input().split()))
ans=0

for car in cars:
    if day==car:
        ans+=1
        
print(ans)