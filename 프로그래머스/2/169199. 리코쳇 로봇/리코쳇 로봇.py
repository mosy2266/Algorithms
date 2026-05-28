from collections import deque

def solution(board):
    h = len(board)
    w = len(board[0])
    start_at = (0,0)
    visited = [[False]*w for _ in range(h)]
    
    for i in range(h):
        line = list(board[i])
        if "R" in line:
            start_at = (i, line.index("R"))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def move(x,y,di):
        while True:
            x += dx[di]
            y += dy[di]
            if x<0 or x>=h or y<0 or y>=w or board[x][y]=="D":
                break
        x -= dx[di]
        y -= dy[di]
        
        return (x,y)
        
    q=deque()
    q.append([*start_at, 0])
    while q:
        x,y,dis = q.popleft()
        for i in range(4):
            nx,ny = move(x,y,i)
            
            if visited[nx][ny]:
                continue
            elif board[nx][ny]=="G":
                return dis+1
            else:
                visited[nx][ny]=True
                q.append([nx,ny,dis+1])
        
    return -1