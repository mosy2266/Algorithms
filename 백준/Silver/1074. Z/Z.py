N,r,c=map(int, input().split())

def solution(n,start,x,y):
    if n==2:
        if x==0 and y==0:
            return start
        elif x==0 and y==1:
            return start+1
        elif x==1 and y==0:
            return start+2
        elif x==1 and y==1:
            return start+3
    
    else:
        mid=n//2

        if x<mid and y<mid:
            start+=0
            x,y=x,y
            return solution(mid,start,x,y)
        elif x<mid and y>=mid:
            start+=mid**2
            x,y=x,y-mid
            return solution(mid,start,x,y)
        elif x>=mid and y<mid:
            start+=2*(mid**2)
            x,y=x-mid,y
            return solution(mid,start,x,y)
        else:
            start+=3*(mid**2)
            x,y=x-mid,y-mid
            return solution(mid,start,x,y)
        
print(solution(2**N,0,r,c))