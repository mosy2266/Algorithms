import sys
input=sys.stdin.readline

series=[]
i=1
ans=''

for _ in range(int(input())):
    num=int(input())

    while i<=num:
        series.append(i)
        ans+="+\n"
        i+=1
    
    if series[-1]==num:
        series.pop()
        ans+="-\n"
    
    else:
        ans="NO"
        break

print(ans)