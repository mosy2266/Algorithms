N=int(input())
dungchi=[]
st=[1]*N

for i in range(N):
    dungchi.append(list(map(int, input().split())))
    dungchi[i].append(1)

for i in range(N):
    for j in range(N):
        if (dungchi[i][0]<dungchi[j][0] and dungchi[i][1]<dungchi[j][1]):
            st[i]+=1

print(*st)