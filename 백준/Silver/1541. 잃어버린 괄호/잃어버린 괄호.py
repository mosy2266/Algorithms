exps=list(input().split("-"))

sums=[]
for exp in exps:
    sums.append(sum(map(int, exp.split('+'))))


ans=sums[0]
for i in range(1, len(sums)):
    ans-=sums[i]
print(ans)