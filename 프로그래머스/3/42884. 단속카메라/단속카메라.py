def solution(routes):
    answer = 0
    n = len(routes)
    camera = -30001
    routes.sort(key= lambda x: x[1])
    
    for route in routes:
        if route[0] > camera:
            camera = route[1]
            answer+=1
        
    return answer