import sys
input=sys.stdin.readline

N=int(input())
cnt_nums=[0]*10001

for _ in range(N):
    num=int(input())
    cnt_nums[num]+=1

for i in range(1, len(cnt_nums)):
    if cnt_nums[i]==0:
        continue
    for _ in range(cnt_nums[i]):
        print(i)