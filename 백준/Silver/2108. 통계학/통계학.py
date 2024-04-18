import sys
input=sys.stdin.readline

N=int(input())
nums=[int(input()) for _ in range(N)]
cnt={} #각 숫자의 개수를 세기 위한 dict
nums.sort()
rg=nums[-1]-nums[0] #범위 계산

if sum(nums)>=0: #산술평균 계산 및 출력
    print(int(sum(nums)/N+0.5))
else:
    print(int(sum(nums)/N-0.5))

print(nums[(N-1)//2]) #중앙값 계산 및 출력

for num in nums: #nums에 있는 숫자들의 개수를 세어 cnt에 추가
    if num in cnt.keys(): #key = 각 숫자, value = 숫자의 개수
        cnt[num]+=1
    else:
        cnt[num]=1

modes=list(cnt.values()) #각 숫자의 개수를 list로 바꿈

if modes.count(max(modes))>1: #최빈값이 여러 개인 경우
    nums_cnt=[]
    for k,v in cnt.items(): #cnt를 순회하며 최빈값에 해당하는 수를 nums_cnt에 추가
        if v==max(modes):
            nums_cnt.append(k)
    print(nums_cnt[1]) #최빈값들 중 두번째로 작은 수 출력

else: #최빈값이 하나 뿐이라면
    for k,v in cnt.items():
        if v==max(modes):
            print(k) #해당 수 출력
            break

print(rg) #범위 출력