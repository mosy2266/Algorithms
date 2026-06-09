import math

def solution(n, k, enemy):    
    def check(target, k, enemy):
        total_enemy = sum(enemy[k:])
        return True if target>=total_enemy else False
    
    def param_search(target, k, enemy):
        l=1
        r=len(enemy)
        max_round=-math.inf
        
        while l<=r:
            mid=(l+r)//2
            cur_round = sorted(enemy[:mid], reverse=True)
            if check(target, k, cur_round):
                l=mid+1
                max_round=mid
            else:
                r=mid-1
        
        return max_round
    
    total_round=len(enemy)
    if k>=total_round: return total_round
    
    answer=param_search(n, k, enemy)
    
    return answer