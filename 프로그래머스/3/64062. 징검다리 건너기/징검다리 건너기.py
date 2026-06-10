def solution(stones, k):
    
    def check(k, mid, stones):
        zeros=0
        for stone in stones:
            if stone>mid:
                zeros=0
            else:
                zeros+=1
            if zeros>=k: return False
        return True
            
    def param_search(k, stones):
        sorted_stones = sorted(stones)
        l = 1
        r = sorted_stones[-1]
        maxFriends = 0
        
        while l<=r:
            mid = (l+r)//2
            if check(k, mid-1, stones):
                l = mid + 1
                maxFriends = mid
            else:
                r = mid - 1
        return maxFriends
    
    answer = param_search(k, stones)
    return answer