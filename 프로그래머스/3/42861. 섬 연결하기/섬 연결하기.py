def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    link = [i for i in range(n)]
    counts = [1]*n
    
    def find(x):
        if link[x] == x:
            return x
        else:
            link[x] = find(link[x])
            return link[x]
    
    def same(x,y):
        return find(x) == find(y)
    
    def unite(x,y):
        x,y = find(x), find(y)
        if x==y: return
        
        if counts[x] < counts[y]:
            x,y = y,x
        
        counts[x]+=counts[y]
        counts[y]=0
        link[y]=x
    
    edges = 0
    for a,b,w in costs:
        if same(a,b): continue

        unite(a,b)
        edges+=1
        answer+=w

        if edges == n-1: break

    return answer