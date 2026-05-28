def solution(triangle):
    answer = 0
    
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    answer = triangle[0][0]
    
    return answer