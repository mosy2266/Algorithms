def solution(name):
    answer = 0
    l = len(name)
    move = l-1
    for x in range(l):
        answer += min(ord(name[x])-ord('A'), ord('Z')-ord(name[x])+1)
        
        y=x+1
        while (y<l and name[y]=='A'):
            y+=1
        
        move = min(move, min(2*x + (l-y), 2*(l-y)+x))
    
    return answer + move