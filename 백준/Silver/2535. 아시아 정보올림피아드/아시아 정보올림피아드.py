import sys
input=sys.stdin.readline

n=int(input())
students=[]
for _ in range(n):
    students.append(list(map(int, input().rstrip().split())))

students=sorted(students, key=lambda x:-x[2])

if students[0][0]!=students[1][0]:
    for i in range(3):
        print(*students[i][:2])

else:
    print(*students[0][:2])
    print(*students[1][:2])
    for i in range(n):
        if students[i][0]!=students[0][0]:
            print(*students[i][:2])
            break