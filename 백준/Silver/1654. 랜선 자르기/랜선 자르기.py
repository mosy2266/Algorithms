import sys
input=sys.stdin.readline

k,n=map(int, input().split())
lans=[int(input()) for _ in range(k)]

def param_search(arr, target):
    start,end=1,max(arr)
    while start<=end:
        mid=(start+end)//2
        cnt=0
        for x in arr:
            cnt+=x//mid
        
        if cnt>=target:
            start=mid+1
        else:
            end=mid-1
    return end

print(param_search(lans, n))