def solution(files):
    lowers = []
    heads = []
    not_heads = []
    numbers = []
    
    for i in range(len(files)):
        lowers.append(files[i].lower())
        
    for lower in lowers:
        for i in range(len(lower)):
            if lower[i].isdigit():
                heads.append(lower[:i])
                not_heads.append(lower[i:i+5])
                break
    
    for not_head in not_heads:
        
        j = -1
        for i in range(len(not_head)):
            if not not_head[i].isdigit():
                j = i
                break
        
        if j == -1:
            numbers.append(int(not_head))
        else:
            numbers.append(int(not_head[:j]))
    
    for i in range(len(files)):
        files[i] = [files[i], heads[i], numbers[i]]
    
    print(files)
    
    files.sort(key=lambda x: (x[1], x[2]))
    
    answer = [x[0] for x in files]
    return answer