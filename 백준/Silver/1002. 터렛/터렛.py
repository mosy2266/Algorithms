import sys
input=sys.stdin.readline

for _ in range(int(input())):
    x_1,y_1,r_1,x_2,y_2,r_2=map(int, input().split())

    if x_1==x_2 and y_1==y_2:
        if r_1==r_2:
            print(-1)
        else:
            print(0)
    else:
        if (x_2-x_1)**2+(y_2-y_1)**2 < (r_2-r_1)**2:
            print(0)
        elif (x_2-x_1)**2+(y_2-y_1)**2 == (r_2-r_1)**2:
            print(1)
        elif (x_2-x_1)**2+(y_2-y_1)**2 < (r_2+r_1)**2:
            print(2)
        elif (x_2-x_1)**2+(y_2-y_1)**2 == (r_2+r_1)**2:
            print(1)
        elif (x_2-x_1)**2+(y_2-y_1)**2 > (r_2+r_1)**2:
            print(0)