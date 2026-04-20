from collections import deque

def solution(maps):
    answer = []
    
    islands = []
    visited = []
    for map in maps:
        map_list=list(map)
        islands.append(map_list)
        visited.append([False]*len(map_list))
    
    island_pos=set()
    for i in range(len(islands)):
        for j in range(len(islands[i])):
            if islands[i][j]!='X':
                island_pos.add((i,j))
    
    if len(island_pos)==0:
        return [-1]
                
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    def bfs(i,j):
        queue=deque([(i,j)])
        ans=0
        
        while queue:
            x,y=queue.popleft()
            
            if visited[x][y]==False:
                ans+=int(islands[x][y])
                visited[x][y]=True

            for i in range(4):
                nx,ny=x+dx[i], y+dy[i]

                if 0<=nx<len(islands) and 0<=ny<len(islands[x]) and islands[nx][ny]!='X' and visited[nx][ny]==False:
                    ans+=int(islands[nx][ny])
                    visited[nx][ny]=True
                    queue.append((nx,ny))
        return ans
    
    while island_pos:
        i,j = island_pos.pop()
        days=bfs(i,j)
        if days>0 : answer.append(days)
    
    answer.sort()
    return answer

