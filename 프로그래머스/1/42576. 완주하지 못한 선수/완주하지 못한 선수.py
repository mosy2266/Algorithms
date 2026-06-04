def solution(participant, completion):
    answer = ''
    
    participants = {}
    completions = {}
    
    for p in participant:
        if p not in participants:
            participants[p]=1
        else:
            participants[p]+=1
    
    for c in completion:
        if c not in completions:
            completions[c]=1
        else:
            completions[c]+=1
    
    for key,value in participants.items():
        if key not in completions or value != completions[key]:
            answer = key
        
    return answer 