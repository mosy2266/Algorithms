import sys
input=sys.stdin.readline

N=int(input())
cards=list(map(int, input().split()))
cards_cnt={}
answer=[]

for _ in range (len(cards)):
    if cards[-1] in cards_cnt.keys():
        cards_cnt[cards.pop()]+=1
    else:
        cards_cnt[cards.pop()]=1

M=int(input())
nums=list(map(int, input().split()))

for num in nums:
    if num in cards_cnt.keys():
        answer.append(str(cards_cnt[num]))
    else:
        answer.append("0")

print(' '.join(answer))