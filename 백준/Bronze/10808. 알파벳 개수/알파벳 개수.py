nums=[0]*26
S=input()
for x in S:
    nums[ord(x)-97]+=1
print(*nums)