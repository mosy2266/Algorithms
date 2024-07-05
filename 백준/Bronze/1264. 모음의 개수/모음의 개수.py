import sys
input=sys.stdin.readline

while True:
    s=input().rstrip()
    cnt=0
    if s=='#':
        break
    s=list(s)
    for x in s:
        if (x=='a' or x=='A' or x=='e' or x=='E' or x=='i' or x=='I' or
        x=='o' or x=='O' or x=='u' or x=='U'):
            cnt+=1
    print(cnt)