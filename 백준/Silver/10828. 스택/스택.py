import sys
input=sys.stdin.readline

N=int(input())
stack=[]

for _ in range(N):
    prcs=input().rstrip()
    if "push" in prcs:
        stack.append(int(prcs[5:]))
    elif prcs=="pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif prcs=="size":
        print(len(stack))
    elif prcs=="empty":
        if stack:
            print(0)
        else:
            print(1)
    elif prcs=="top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

'''prcs=="pop" << 이렇게 조건식을 쓰려면
.rstrip()(맨 오른쪽 문자 제거)을 사용해서 개행문자를 제거해줘야 함
왜냐면 sys.stdin.readline은 한 줄 단위로 입력받기 때문에 \n도 함께 들어오기 때문,,'''