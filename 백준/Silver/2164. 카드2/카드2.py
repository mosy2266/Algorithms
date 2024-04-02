from collections import deque

N=int(input())
cards=[i for i in range(1,N+1)]
cards_queue=deque(cards)

while (len(cards_queue)>1):
    cards_queue.popleft()
    cards_queue.rotate(-1)

print(cards_queue[0])