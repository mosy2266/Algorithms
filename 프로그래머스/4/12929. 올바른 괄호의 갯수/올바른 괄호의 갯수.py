import math

def solution(n):
    answer = 0
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        answer = math.factorial(2*n) / (math.factorial(n+1)*math.factorial(n))

    return answer