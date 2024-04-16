import sys
input=sys.stdin.readline

nums=[]
for _ in range(int(input())):
    num=int(input())
    if num!=0:
        nums.append(num)
    else:
        nums.pop()

print(sum(nums))