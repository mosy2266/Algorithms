def solution(n):
    answer = []
        
    def hanoi(n,start,end,tran):
        if n==1:
            answer.append([start, end])
            return
        hanoi(n-1, start, tran, end)
        answer.append([start,end])
        hanoi(n-1, tran, end, start)
    
    hanoi(n,1,3,2)
    
    return answer