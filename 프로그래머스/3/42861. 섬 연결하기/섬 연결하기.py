def solution(n, costs):
    answer = 0
    
    #연결 정보 배열 초기화
    link = [i for i in range(n)]
    
    #유니온 파인드 함수 정의
    def find(x):
        if link[x] == x:
            return x
        else:
            link[x] = find(link[x])
            return link[x]
    
    def same(x,y):
        if find(x) == find(y):
            return True
        else: 
            return False
    
    def unite(x,y):
        x,y = find(x), find(y)
        if x==y : return
    
        link[y] = x
    
    #풀이 코드
    edges = 0
    costs.sort(key=lambda x: x[2])
    for a,b,cost in costs:
        if same(a,b) : continue
        
        unite(a,b)
        answer+=cost
        edges+=1
        
        if edges == n-1:
            break
        
    return answer