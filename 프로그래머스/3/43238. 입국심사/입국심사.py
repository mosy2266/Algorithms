import math

def solution(n, times):    
    def check(target, takenTime, times):
        cur = 0
        
        for time in times:
            cur += takenTime//time
        
        return True if cur>=target else False
    
    def param_search(target, times):
        l = 1
        r = times[-1] * target
        minTime = math.inf
        
        while l<=r:
            m = (l+r)//2
            if check(target, m, times):
                r = m-1
                minTime = m
            else:
                l = m+1
        return minTime
        
    times.sort()
    answer = param_search(n, times)
    
    return answer