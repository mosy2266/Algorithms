def solution(dirs):
    answer = 0
    prev_x, prev_y = 0, 0
    now_x, now_y = 0, 0
    
    visited = set()
    
    for d in dirs:
        prev_x, prev_y = now_x, now_y
        if d == "U" and -5<=now_y + 1<=5:
            now_y += 1
        elif d == "D" and -5<=now_y - 1<=5:
            now_y -= 1
        elif d == "R" and -5<=now_x + 1<=5:
            now_x += 1
        elif d == "L" and -5<=now_x - 1<=5:
            now_x -= 1
        
        
        if (prev_x,prev_y,now_x,now_y) not in visited:
            if prev_x == now_x and prev_y == now_y: continue
            answer+=1
            visited.add((prev_x,prev_y,now_x,now_y))
            visited.add((now_x,now_y,prev_x,prev_y))
        
    return answer