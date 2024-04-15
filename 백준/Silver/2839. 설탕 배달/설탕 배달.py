N=int(input())
sugar=[5001]*(N+1)
kg=[3,5]

sugar[0]=0

for i in range(2):
    for j in range(kg[i], N+1):
        if sugar[j-kg[i]]!=5001:
            sugar[j]=min(sugar[j], sugar[j-kg[i]]+1)

if sugar[N]==5001:
    print(-1)
else:
    print(sugar[N])