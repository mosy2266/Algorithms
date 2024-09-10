l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())

if a%c==0: kor=a//c
else: kor=a//c+1

if b%d==0: math=b//d
else: math=b//d+1

print(l-max(kor, math))