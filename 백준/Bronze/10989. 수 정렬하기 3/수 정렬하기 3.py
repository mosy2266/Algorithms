import sys
input=sys.stdin.readline

N=int(input())
#가능한 수의 범위가 1~10000이므로 10001의 크기를 가지도록 선언(인덱스 매칭 편하게)
cnt_nums=[0]*10001

for _ in range(N): #수를 입력 받으면서 해당 수를 인덱스로 하는 cnt_nums의 값을 1씩 증가
    cnt_nums[int(input())]+=1

for i in range(1, len(cnt_nums)):
    if cnt_nums[i]!=0: #개수가 0이라면 출력 X
        for _ in range(cnt_nums[i]):
            print(i)