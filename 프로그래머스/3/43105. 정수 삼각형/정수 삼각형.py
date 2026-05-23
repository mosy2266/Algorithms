def solution(triangle):
    answer = 0
    n = len(triangle)
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    answer = triangle[0][0]
    
    return answer