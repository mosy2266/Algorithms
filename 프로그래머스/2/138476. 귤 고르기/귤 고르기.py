def solution(k, tangerine):
    answer = 0
    heaviest = max(tangerine)
    
    counts = [0]*(heaviest+1)
    
    for t in tangerine:
        counts[t]+=1
    
    counts.sort(reverse=True)
    
    count = 0
    for c in counts:
        count+=c
        answer+=1
        if count>=k: break
        
    
    return answer