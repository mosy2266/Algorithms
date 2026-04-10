import sys
input=sys.stdin.readline

s=input().rstrip()
t=input().rstrip()

added_str=[]

def addA(string):
    return string+"A"

def addB(string):
    string=string+"B"
    return string[-1::-1]

def solution(s,t):
    if len(s)==len(t):
        added_str.append(s)
        return

    add_a=addA(s)
    add_b=addB(s)

    if add_a in t or add_a[-1::-1] in t:
        solution(add_a, t)
    
    if add_b in t or add_b[-1::-1] in t:
        solution(add_b, t)
    
solution(s,t)

if t in added_str:
    print(1)
else:
    print(0)