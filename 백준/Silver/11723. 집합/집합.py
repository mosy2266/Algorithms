import sys
input=sys.stdin.readline

class sets:
    def __init__(self):
        self.items=set()
    
    def add(self, x):
        if x not in self.items:
            self.items.add(x)

    def remove(self, x):
        if x in self.items:
            self.items.remove(x)
    
    def check(self, x):
        if x in self.items:
            print(1)
        else:
            print(0)
    
    def toggle(self, x):
        if x in self.items:
            self.items.remove(x)
        else:
            self.items.add(x)
    
    def all(self):
        self.items.update([i for i in range(1,21)])
    
    def empty(self):
        self.items.clear()

S=sets()
for _ in range(int(input())):
    prcs=input().rstrip()
    
    if "add" in prcs:
        num=int(prcs[4:])
        S.add(num)
    elif "remove" in prcs:
        num=int(prcs[7:])
        S.remove(num)
    elif "check" in prcs:
        num=int(prcs[6:])
        S.check(num)
    elif "toggle" in prcs:
        num=int(prcs[7:])
        S.toggle(num)
    elif prcs=="all":
        S.all()
    elif prcs=="empty":
        S.empty()