import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

sorted_B=sorted(B, reverse=True)
A.sort()

sum=0
for i in range(N):
    sum+=A[i]*sorted_B[i]

print(sum)