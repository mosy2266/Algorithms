N,M=map(int, input().split())
cards=sorted(list(map(int, input().split())), reverse=True)

result=0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum=cards[i]+cards[j]+cards[k]
            if sum<=M:
                if result<sum:
                    result=sum
                break

print(result)