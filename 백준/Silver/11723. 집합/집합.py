import sys
input=sys.stdin.readline

S=set()

for _ in range(int(input())):
    prcs=input().rstrip()

    if "add" in prcs:
        S.add(int(prcs[4:]))
    elif "remove" in prcs:
        S.discard(int(prcs[7:]))
    elif "check" in prcs:
        num=int(prcs[6:])
        print(1) if num in S else print(0)
    elif "toggle" in prcs:
        num=int(prcs[7:])
        S.remove(num) if num in S else S.add(num)
    elif prcs=="all":
        S.update([i for i in range(1,21)])
    elif prcs=="empty":
        S.clear()