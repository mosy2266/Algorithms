def solution(record):
    answer = []
    nicknames = {}

    result = []
    for r in record:
        if r[:5] == "Enter":
            task, uid, nickname = r.split(" ")
            nicknames[uid] = nickname
            result.append(("님이 들어왔습니다.", uid))
            continue
        
        if r[:5] == "Leave":
            task, uid = r.split(" ")
            result.append(("님이 나갔습니다.", uid))
            continue
        
        if r[:6] == "Change":
            task, uid, nickname = r.split(" ")
            nicknames[uid] = nickname
    
    for line, uid in result:
        answer.append(nicknames[uid]+line)
        
    return answer