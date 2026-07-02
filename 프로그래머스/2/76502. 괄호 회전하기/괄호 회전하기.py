from collections import deque

def solution(s):
    answer = 0
    brackets = {'[':3, '{':2, '(':1, ']':-3, '}':-2, ')':-1}
    queue = deque(list(s))
    
    for i in range(len(s)):
        queue.rotate(-1)
        if brackets[queue[0]] < 0 or brackets[queue[-1]] > 0: continue
        
        bracket = ''.join(queue)
        stack = []
        
        for b in bracket:
            if not stack:
                stack.append(b)
                continue
            if brackets[stack[-1]] < 0 : break
            
            if brackets[stack[-1]] * brackets[b] < 0 and brackets[stack[-1]] + brackets[b] != 0:
                break
            
            if brackets[stack[-1]] + brackets[b] == 0:
                stack.pop()
                continue
            else:
                stack.append(b)
        
        if not stack:
            answer+=1
        
    return answer