import sys
input=sys.stdin.readline

class stack:
    def __init__(self):
        self.items=[]
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            print(self.items.pop())
        else:
            print(-1)
    
    def size(self):
        print(len(self.items))
    
    def empty(self):
        if self.items:
            print(0)
        else:
            print(1)
    
    def top(self):
        if self.items:
            print(self.items[-1])
        else:
            print(-1)

N=int(input())
ex=stack()

for _ in range(N):
    prcs=input()
    if "push" in prcs:
        num=int(prcs[5:])
        ex.push(num)
    else:
        if "pop" in prcs:
            ex.pop()
        elif "size" in prcs:
            ex.size()
        elif "empty" in prcs:
            ex.empty()
        elif "top" in prcs:
            ex.top()