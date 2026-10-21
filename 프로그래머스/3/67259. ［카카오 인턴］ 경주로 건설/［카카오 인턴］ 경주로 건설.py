from collections import deque

def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cost_board = [[[float('inf')]*4 for _ in range(n)] for _ in range (n)]
    
    q = deque()
    
    for i in range(4):
        q.append((0,0,0,i))
        cost_board[0][0][i] = 0
        
    while q:
        x, y, cost, di = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                new_cost = cost + 100 if di == i else cost + 600

                if new_cost < cost_board[nx][ny][i]:
                    cost_board[nx][ny][i] = new_cost
                    q.append((nx, ny, new_cost, i))
                        
    return min(cost_board[n-1][n-1])