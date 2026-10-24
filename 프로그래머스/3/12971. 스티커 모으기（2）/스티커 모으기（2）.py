def solution(sticker):
    n = len(sticker)
    
    if n==1:
        return sticker[0]
    
    if n==2:
        return max(sticker[0], sticker[1])

    dp1 = [0]*(n-1)
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
        
    dp2 = [0]*n
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])    
    
    return max(dp1[-1], dp2[-1])