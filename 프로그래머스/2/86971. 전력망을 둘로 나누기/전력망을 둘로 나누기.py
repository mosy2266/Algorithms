from collections import deque

def solution(n, wires):
    answer = int(10**3)
    
    for i in range(n-1):
        wire_queue = deque(wires)
        adj=[[] for _ in range(n)]
        visited=[False]*n
        
        wire_queue.rotate(i)
        cut_a, cut_b = wire_queue.popleft()
        
        for wire in wire_queue:
            a,b = wire
            adj[a-1].append(b)
            adj[b-1].append(a)
        
        a_cnt = bfs(cut_a, adj, visited)
        b_cnt = bfs(cut_b, adj, visited)
        
        answer = min(answer, abs(a_cnt-b_cnt))
    
    return answer

def bfs(start, graph, visited):
    cnt=1
    queue = deque(graph[start-1])
    visited[start-1] = True
    
    if not queue:
        return cnt

    while queue:
        v = queue.popleft()
        visited[v-1]=True
        cnt+=1
        for i in graph[v-1]:
            if not visited[i-1]:
                queue.append(i)
                visited[i-1]=True
    return cnt