from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    
    if cacheSize > 0 :
        for x in cities:
            city = x.upper()
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.append(city)
            else:
                answer += 5
                if len(cache) >= cacheSize:
                    cache.popleft()
                cache.append(city)
    else:
        answer = len(cities) * 5
    
    return answer