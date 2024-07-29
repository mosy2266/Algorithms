ans=0
lst=99
for _ in range(7):
    num=int(input())
    if num%2!=0:
        ans+=num
        lst=min(lst,num)

if ans:
    print(ans)
    print(lst)
else:
    print(-1)