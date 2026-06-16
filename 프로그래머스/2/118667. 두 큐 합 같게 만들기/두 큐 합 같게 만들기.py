from collections import deque

def solution(queue1, queue2):
    answer = 0
    new_queue = queue1 + queue2
    new_sum = sum(new_queue)
    
    if new_sum % 2 != 0: return -1
    
    target = new_sum // 2
    
    l,r,cur = 0, len(queue1), sum(queue1)
    
    while l<r<=len(new_queue):
        if cur<target:
            if r<len(new_queue):
                cur += new_queue[r]
                r+=1
                answer+=1
            else:
                return -1
        elif cur>target:
            cur -= new_queue[l]
            l+=1
            answer+=1
        else:
            return answer
        
    
    return -1