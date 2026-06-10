from collections import deque

def solution(info, edges):
    answer = 1
    visited = [False] * (1<<17)
    visited[(1<<0)] = True
    
    q = deque()
    q.append((1<<0))
    
    while q:
        cur_state = q.popleft()
        
        for p,c in edges:
            next_state = cur_state | (1<<c)
            if (cur_state & (1<<p)) and not (cur_state & (1<<c)) and not visited[next_state]:
                sheep, wolf = 0, 0
                
                for node in range(len(info)):
                    if not(next_state & (1<<node)): continue
                    
                    sheep += info[node] ^ 1
                    wolf += info[node]
                
                if wolf < sheep:
                    answer = max(answer, sheep)
                    q.append(next_state)
                    visited[next_state]=True
    
    return answer