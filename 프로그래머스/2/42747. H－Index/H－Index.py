def solution(citations):
    answer = 0
    citations.sort()
    
    if citations[-1]==0:
        return 0
    
    for i in range(len(citations)-1):
        for j in range(citations[i], citations[i+1]):
            if j==citations[i]:
                if (len(citations)-i)>=j:
                    answer = max(answer, j)
            if j>citations[i]:
                if (len(citations)-1-i)>=j:
                    answer = max(answer, j)
    
    if answer==0:
        return len(citations)
    
    return answer