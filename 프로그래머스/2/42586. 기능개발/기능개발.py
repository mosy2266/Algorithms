from collections import deque

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    
    remain = [100]*n
    
    for i in range(n):
        remain[i] -= progresses[i]
        
        if remain[i] % speeds[i] == 0:
            remain[i] //= speeds[i]
        else:
            remain[i] = remain[i]//speeds[i] + 1
    
    queue = deque(remain)
    
    while queue:
        cnt = 0
        release = queue.popleft()
        cnt += 1
        while queue:
            if release >= queue[0]:
                queue.popleft()
                cnt += 1
            else:
                break
        answer.append(cnt)
                
    return answer