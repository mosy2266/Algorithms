import sys
input=sys.stdin.readline

while True:
    s=input().rstrip()
    cnt=0
    if s=='#':
        break
    s=list(s.lower())
    for x in s:
        if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
            cnt+=1
    print(cnt)