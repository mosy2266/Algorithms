N=int(input())

min_num=0
for i in range((10**(len(str(N))-1))//2, N):
    div_sum=i
    num=i
    k=6
    while k>=1:
        a=num//(10**k)
        div_sum+=a
        num-=a*(10**k)
        k-=1
    div_sum+=num
    if div_sum==N:
        min_num=i
        break;

print(min_num)