import sys
input=sys.stdin.readline

N=int(input())
paper=[]
blue_ans=0
white_ans=0

for _ in range(N):
    paper.append(list(map(int, input().rstrip().split())))

def solution(n,arr):
    global blue_ans, white_ans
    cnt=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                cnt+=1
    if cnt==n*n:
        blue_ans+=1
    elif cnt==0:
        white_ans+=1
    else:
        new_paper=[]
        for i in range(n//2):
            new_paper.append(arr[i][:n//2])
        solution(n//2, new_paper)

        new_paper=[]
        for i in range(n//2):
            new_paper.append(arr[i][n//2:])
        solution(n//2, new_paper)

        new_paper=[]
        for i in range(n//2, n):
            new_paper.append(arr[i][:n//2])
        solution(n//2, new_paper)

        new_paper=[]
        for i in range(n//2, n):
            new_paper.append(arr[i][n//2:])
        solution(n//2, new_paper)

solution(N, paper)
print(white_ans)
print(blue_ans)