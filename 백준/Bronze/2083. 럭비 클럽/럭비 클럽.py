import sys
input=sys.stdin.readline

while True:
    name,age,weight=input().rstrip().split()
    if name=='#':
        break
    elif int(age)>17 or int(weight)>=80:
        print(name, "Senior")
    else:
        print(name, "Junior")