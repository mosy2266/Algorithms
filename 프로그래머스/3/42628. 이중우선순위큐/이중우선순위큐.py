def solution(operations):
    answer = [0,0]
    q = []
    
    for o in operations:
        if o[0]=="I":
            num = int(o[2:])
            q.append(num)
        else:
            if q:
                if o[2]=="-":
                    q.remove(min(q))
                else:
                    q.remove(max(q))
    
    if q:
        answer[0], answer[1] = max(q), min(q)
    
    return answer