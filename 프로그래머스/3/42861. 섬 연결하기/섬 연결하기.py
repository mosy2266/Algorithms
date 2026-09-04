def solution(n, costs):
    answer = 0
    link = [i for i in range(n)]
    
    def find(x):
        if link[x] == x:
            return x
        else:
            link[x] = find(link[x])
            return link[x]
    
    def same(x,y):
        return find(x)==find(y)
    
    def unite(x,y):
        x,y = find(x), find(y)
        if x==y: return
        link[y] = x
    
    edges = 0
    costs.sort(key= lambda x: x[2])
    
    for a,b,w in costs:
        if same(a,b): continue
        
        unite(a,b)
        answer+=w
        edges+=1
        
        if edges == n-1: break
        
    return answer