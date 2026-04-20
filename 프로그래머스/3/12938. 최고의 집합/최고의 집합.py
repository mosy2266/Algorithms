def solution(n, s):
    answer = []
    
    for i in range(n,0,-1):
        num=int(s/i)
        if num==0:
            return [-1]
        s=s-num
        answer.append(num)
    
    answer.sort()
    return answer