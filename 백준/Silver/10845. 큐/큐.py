import sys
input=sys.stdin.readline

class queue:
    def __init__(self):
        self.items=[]
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            return self.items.pop(0)
        else:
            return -1
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        if self.items:
            return 0
        else:
            return 1
    
    def front(self):
        if self.items:
            return self.items[0]
        else:
            return -1
    
    def back(self):
        if self.items:
            return self.items[-1]
        else:
            return -1

N=int(input())
ex=queue()

for _ in range(N):
    prcs=input().rstrip()
    if "push" in prcs:
        ex.push(int(prcs[5:]))
    elif prcs=="pop":
        print(ex.pop())
    elif prcs=="size":
        print(ex.size())
    elif prcs=="empty":
        print(ex.empty())
    elif prcs=="front":
        print(ex.front())
    elif prcs=="back":
        print(ex.back())