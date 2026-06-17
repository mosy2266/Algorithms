import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0]<K:
        
        if len(scoville)==1: return -1
        
        min_sc = heapq.heappop(scoville)
        second_sc = heapq.heappop(scoville)
        new_sc = min_sc + 2 * second_sc
        answer+=1
        heapq.heappush(scoville, new_sc)
    
    return answer