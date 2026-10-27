def solution(s):
    answer = []
    sets = list(s[2:-2].split("},{"))
    sets.sort(key=lambda x: len(x))
    
    num_set = set()
    
    for n in sets:
        num = list(map(int, n.split(",")))
        for i in num:
            if i not in num_set:
                num_set.add(i)
                answer.append(i)
            else:
                continue
        
    return answer