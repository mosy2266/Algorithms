n=int(input())

dp=[0,1,2,3]

for i in range(4,n+1):
    squares=4
    j=1
    while (j**2)<=i:
        squares=min(squares, dp[i-j**2])
        j+=1
    dp.append(squares+1)

print(dp[n])