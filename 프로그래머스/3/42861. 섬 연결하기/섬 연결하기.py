def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    link = [i for i in range(n)]
    sz = [1]*n
        
    def find(x):
        if link[x]==x: return x
        else:
            link[x] = find(link[x])
            return link[x]
    
    def same(a,b):
        return find(a) == find(b)
    
    def unite(a,b):
        a,b = find(a), find(b)
        if a==b: return
        
        if sz[a] < sz[b]:
            a,b=b,a
        sz[a] += sz[b]
        sz[b] = 0
        link[b] = a
    
    edges=0
    for cost in costs:
        x,y,w = cost
        
        if same(x,y):
            continue
        answer+=w
        unite(x,y)
        edges+=1
        
        if edges == n-1:
            break
            
    return answer