

def solution(info, edges):
    answer = 0
    graph = [[] for _ in range (len(info))]
    
    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    def dfs(cur, sheep, wolf, nodes):
        nonlocal answer
        
        sheep += info[cur]^1
        wolf += info[cur]
        answer = max(answer, sheep)
        
        next_nodes = nodes + graph[cur]
        if cur in next_nodes: next_nodes.remove(cur)
        
        if wolf>=sheep:
            return
        
        for n in next_nodes:
            dfs(n, sheep, wolf, next_nodes[:])
    
    dfs(0,0,0,[])
    return answer