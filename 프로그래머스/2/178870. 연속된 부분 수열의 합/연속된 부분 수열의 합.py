def solution(sequence, k):    
    if k in sequence:
        return [sequence.index(k), sequence.index(k)]

    n = len(sequence)
    l,r,temp = 0,0,0
    minimum = float('inf')
    
    while r<n:
        temp += sequence[r]
        r += 1
        if temp > k:
            while temp > k:
                temp -= sequence[l]
                l += 1
        
        if temp == k:
            if r-1-l < minimum:
                minimum = r-1-l
                answer = [l, r-1]
    
    return answer