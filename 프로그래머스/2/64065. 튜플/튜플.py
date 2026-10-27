def solution(s):
    answer = []
    sets = list(s[2:-2].split("},{"))
    sets.sort(key=lambda x: len(x))
        
    for n in sets:
        num = list(map(int, n.split(",")))
        for i in num:
            if i not in answer:
                answer.append(i)
            
    return answer