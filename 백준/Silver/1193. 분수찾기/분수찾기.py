x=int(input())
n=1

while x>n:
    x-=n
    n+=1

if n%2==0:
    num=x
    denom=n+1-x
else:
    num=n+1-x
    denom=x

print(f'{num}/{denom}')