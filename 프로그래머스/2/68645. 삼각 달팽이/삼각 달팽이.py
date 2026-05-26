def solution(n):
    answer = []
    snails = [[0]*i for i in range(1,n+1)]
    
    dx=[1,0,-1]
    dy=[0,1,-1]
    
    x,y,k = -1,0,1
    cnt=0
    while n>0:
        if (cnt%3==0):
            for i in range(n):
                x+=dx[0]
                y+=dy[0]
                snails[x][y]=k
                k+=1
                
        elif(cnt%3==1):
            for i in range(n):
                x+=dx[1]
                y+=dy[1]
                snails[x][y]=k
                k+=1
        
        elif(cnt%3==2):
            for i in range(n):
                x+=dx[2]
                y+=dy[2]
                snails[x][y]=k
                k+=1
        n-=1
        cnt+=1
    
    answer = sum(snails, [])
    return answer