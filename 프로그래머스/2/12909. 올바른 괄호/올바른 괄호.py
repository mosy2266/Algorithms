def solution(s):
    if s[-1]=="(": return False
    
    stack = []
    
    for i in range(len(s)):
        if not stack: 
            stack.append(s[i])
            continue
            
        if stack[-1]==')':
            return False
        
        if stack[-1] != s[i]:
            stack.pop()
            continue
        else:
            stack.append(s[i])

    if not stack:
        return True
    return False