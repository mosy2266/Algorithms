import sys

def solution(numbers, target):
    answer = 0    
    
    def bfs(cnt, idx):
        nonlocal answer
        
        if idx == len(numbers):
            if cnt == target:
                answer+=1
            return
        
        cnt_plus = cnt + numbers[idx]
        cnt_minus = cnt - numbers[idx]
        idx+=1
        
        bfs(cnt_plus, idx)
        bfs(cnt_minus, idx)
    
    bfs(0,0)
    
    return answer