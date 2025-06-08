import sys
input=sys.stdin.readline

isbn=input()
num=0

for i in range(13):
    if (isbn[i]!='*' and i%2==0):
        num+=int(isbn[i])
    elif (isbn[i]!='*' and i%2!=0):
        num+=int(isbn[i])*3
    
if num%10==0:
    print(0)
else:
    for j in range(10):
        if isbn.find('*')%2==0:
            if (num+j)%10==0:
                print(j)
                break
        else:
            if (num+3*j)%10==0:
                print(j)
                break