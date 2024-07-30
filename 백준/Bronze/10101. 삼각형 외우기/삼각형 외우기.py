a=int(input())
b=int(input())
c=int(input())
angle=a+b+c

if angle==180:
    if a==b and b==c:
        print("Equilateral")
    elif a==b or b==c or c==a:
        print("Isosceles")
    elif a!=b and b!=c and c!=a:
        print("Scalene")
else:
    print("Error")