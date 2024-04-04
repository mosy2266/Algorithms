import sys
input=sys.stdin.readline

class deque:
    def __init__(self):
        self.queue=[]
    
    def push_front(self, item):
        self.queue.insert(0,item)
    
    def push_back(self, item):
        self.queue.append(item)
    
    def pop_front(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1
        
    def pop_back(self):
        if self.queue:
            return self.queue.pop()
        else:
            return -1
    
    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return 0
        else:
            return 1
    
    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1

N=int(input())
ex=deque()

for _ in range(N):
    prcs=input().rstrip()
    if "push_front" in prcs:
        ex.push_front(int(prcs[11:]))
    elif "push_back" in prcs:
        ex.push_back(int(prcs[10:]))
    elif prcs=="pop_front":
        print(ex.pop_front())
    elif prcs=="pop_back":
        print(ex.pop_back())
    elif prcs=="size":
        print(ex.size())
    elif prcs=="empty":
        print(ex.empty())
    elif prcs=="front":
        print(ex.front())
    elif prcs=="back":
        print(ex.back())