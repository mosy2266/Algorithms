import sys
input=sys.stdin.readline

N=int(input())

for _ in range (N):
    PS=input().rstrip()
    while "()" in PS:
        PS=PS.replace("()","")
    if not PS:
        print("YES")
    else:
        print("NO")

#모든 VPS는 "()"로 이루어져 있음을 이용해 풀이
#.remove() 메서드는 문자열에서 사용 불가 -> .replace() 메서드를 사용
