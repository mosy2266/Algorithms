from collections import deque

def solution(n, results):
    answer = 0
    win=[[] for _ in range (n+1)]
    lose=[[] for _ in range (n+1)]
    
    for result in results:
        winner, loser = result
        win[winner].append(loser)
        lose[loser].append(winner)
    
    print(win)
    print(lose)
    
    def bfs(start, graph, visited):
        cnt=0
        queue=deque([start])
        
        while queue:
            v=queue.popleft()
            visited[v]=True
            
            for i in graph[v]:
                if not visited[i]:
                    visited[i]=True
                    queue.append(i)
                    cnt+=1
        return cnt
    
    for i in range(1, n+1):
        visited=[False]*(n+1)
        win_cnt = bfs(i, win, visited)
        lose_cnt = bfs(i, lose, visited)
        
        if win_cnt + lose_cnt == n-1:
            answer+=1
            
    return answer