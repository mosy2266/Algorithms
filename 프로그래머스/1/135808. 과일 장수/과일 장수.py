def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(len(score)//m):
        start=m*i
        if start+m>len(score) : end=len(score)
        else : end=start+m
        
        nums=score[start:end]
        answer+=min(nums)*m
    
    return answer