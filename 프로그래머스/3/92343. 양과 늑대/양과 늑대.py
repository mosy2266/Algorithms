from collections import deque

def solution(info, edges):
    answer = 1
    visited = [False] * (1<<17)
    visited[(1<<0)] = True
    
    q=deque()
    q.append((1<<0))
    
    while q:
        cur_node = q.popleft()
        for p,c in edges:
            next_nodes = (cur_node | (1<<c))
            if (cur_node & (1<<p)) and not (cur_node & (1<<c)) and not visited[next_nodes]:
                wolf, sheep = 0, 0
                
                for node in range(len(info)):
                    if (next_nodes & (1<<node)) == 0 : continue
                    sheep += info[node] ^ 1
                    wolf += info[node]
                    
                if wolf < sheep:
                    answer = max(answer, sheep)
                    visited[next_nodes] = True
                    q.append(next_nodes)
    
    return answer