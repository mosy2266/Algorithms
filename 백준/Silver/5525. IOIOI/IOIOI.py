n=int(input())
m=int(input())
s=input()

p_n=""

for i in range(1, 2*n+2):
    if i%2!=0:
        p_n+='I'
    else:
        p_n+='O'

cnt=0
for i in range(len(s)-len(p_n)+1):
    sub=s[i:i+len(p_n)]
    if sub==p_n:
        cnt+=1

print(cnt)