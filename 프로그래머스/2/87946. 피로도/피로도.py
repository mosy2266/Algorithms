from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    perm = list(permutations(dungeons))
    
    for p in perm:
        fatigue = k
        count = 0
        
        for f in p:
            if f[0] > fatigue: break
            else:
                fatigue -= f[1]
                count += 1
        answer = max(answer, count)
    
    return answer