import sys
sys.setrecursionlimit(10**4)

def solution(nodeinfo):
    answer = [[], []]
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    nodeinfo.sort(key = lambda x: x[0])
    
    def trav(nodes):
        if nodes:
            root=(0,-1,0)
            for idx, (x,y,v) in enumerate(nodes):
                if y > root[1]:
                    root=(idx,y,v)
            answer[0].append(root[-1])
            left, right=nodes[:root[0]], nodes[root[0]+1:]
            trav(left)
            trav(right)
            answer[1].append(root[-1])
    
    trav(nodeinfo) 
    return answer

