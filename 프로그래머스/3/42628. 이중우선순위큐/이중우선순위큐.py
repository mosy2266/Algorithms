import heapq

def solution(operations):
    answer = [0,0]
    max_h = []
    min_h = []
    
    for o in operations:
        if o[0]=='I':
            num = int(o[2:])
            heapq.heappush(max_h, -num)
            heapq.heappush(min_h, num)
        else:
            if max_h or min_h:
                if o[2]=='-':
                    num = heapq.heappop(min_h)
                    if -num in max_h: max_h.remove(-num)
                else:
                    num = -heapq.heappop(max_h)
                    if num in min_h: min_h.remove(num)
    
    if max_h:
        answer[0] = -heapq.heappop(max_h)
    
    if min_h:
        answer[1] = heapq.heappop(min_h)
    
    return answer