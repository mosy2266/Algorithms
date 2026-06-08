import math

def solution(clothes):
    answer = 1
    closet={}
    
    for c in clothes:
        if c[1] in closet.keys():
            closet[c[1]] += 1
        else:
            closet[c[1]] = 1
    
    types_cnt = len(closet.keys())
    
    for key in closet.keys():
        cnt = closet[key]+1
        answer*=cnt
        
    return answer-1