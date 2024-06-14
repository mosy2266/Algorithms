import sys
input=sys.stdin.readline

n,m=map(int, input().rstrip().split())
trees=list(map(int, input().rstrip().split()))

def param_search(arr, target):
    start,end=1,max(arr)
    while start<=end:
        mid=(start+end)//2
        cnt=0
        for x in arr:
            if x-mid>0:
                cnt+=x-mid
            else:
                cnt+=0
        
        if cnt>=target:
            start=mid+1
        else:
            end=mid-1
    return end

print(param_search(trees, m))