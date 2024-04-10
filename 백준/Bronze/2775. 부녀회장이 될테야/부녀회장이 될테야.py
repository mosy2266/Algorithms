T=int(input())

for _ in range (T):
    k=int(input())
    n=int(input())
    zero_floor=[list(i for i in range(1,n+1))]
    for i in range(k):
        floor=[]
        for j in range(n):
            nth_room=0
            for x in range(j+1):
                nth_room+=zero_floor[i][x]
            floor.append(nth_room)
        zero_floor.append(floor)
    print(zero_floor[k][n-1])