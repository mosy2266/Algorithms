import math

def solution(n, k, enemy):
    def check(target, k, mid, enemies):
        total_enemies = sum(enemies[k:mid])
        return True if target>=total_enemies else False
    
    def param_search(target, k, enemy):
        l = 1
        r = len(enemy)
        maxRound = -math.inf
        
        while l<=r:
            mid = (l+r)//2
            enemies = sorted(enemy[:mid], reverse=True)
            if check(target, k, mid, enemies):
                l = mid+1
                maxRound = mid
            else:
                r = mid-1
        return maxRound
    
    answer = param_search(n,k,enemy)
    return answer