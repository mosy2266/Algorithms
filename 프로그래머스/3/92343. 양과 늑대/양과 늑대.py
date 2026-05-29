import sys
sys.setrecursionlimit(10**6)

def solution(info, edges):
    graph=[[] for _ in range(len(info))]
    visited=[False]*len(info)
    
    for edge in edges:
        graph[edge[0]].append(edge[1])
        
    answer = 0
    def dfs(cur, sheep, wolf, nodes):
        nonlocal answer
        sheep+=info[cur]^1
        wolf+=info[cur]
        
        next_nodes = nodes + graph[cur]
        
        if cur in next_nodes: next_nodes.remove(cur)
        
        answer=max(answer, sheep)
        
        if wolf>=sheep:
            return
        
        for n in next_nodes:
            dfs(n, sheep, wolf, next_nodes[:])
    
    dfs(0,0,0,[])
    return answer