import sys
input=sys.stdin.readline

n,m=map(int, input().rstrip().split())
trees=list(map(int, input().rstrip().split()))

def param_search(arr, target):
    start,end=1,max(arr) #탐색의 시작점을 1, 끝점을 가장 높은 나무의 높이
    while start<=end:
        mid=(start+end)//2 #매 탐색마다 절단기에 설정할 높이
        cnt=0
        for x in arr: #설정된 높이로 각 나무를 자르는 과정
            if x>mid: #설정된 높이보다 나무가 크면
                cnt+=x-mid #더해줌

        if cnt>=target: #잘린 나무들의 길이 합이 원하는 총 길이보다 같거나 크다면
            start=mid+1 #시작점을 이동
        else: #작다면
            end=mid-1 #끝점을 이동
    return end #끝점이 시작점보다 작아지는 순간의 값이 정답

print(param_search(trees, m))