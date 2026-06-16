from collections import deque

def solution(maps):
    n = len(maps[0])
    m = len(maps)
    visited=[[False]*n for _ in range(m)]
    
    def bfs(a,b):
        q = deque([(a,b)])
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        while q:
            x,y = q.popleft()
            visited[x][y]=True
        
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]

                if 0<=nx<m and 0<=ny<n and maps[nx][ny]!=0 and not visited[nx][ny]:
                    maps[nx][ny] = maps[x][y]+1
                    visited[nx][ny] = True
                    q.append((nx,ny))
    
    bfs(0,0)
    
    if maps[m-1][n-1]==1:
        return -1
    else:
        return maps[m-1][n-1]