def solution(msg):
    answer = []
    dictionary = {}
    
    for i in range(65,91):
        dictionary[chr(i)] = i-64
    
    idx = 27
    w = ''
    for i in range(len(msg)):
        w += msg[i]
        
        if i == len(msg)-1:
            answer.append(dictionary[w])
            break
        
        if w+msg[i+1] not in dictionary:
            dictionary[w+msg[i+1]] = idx
            idx += 1
            answer.append(dictionary[w])
            w = ''
        
    return answer