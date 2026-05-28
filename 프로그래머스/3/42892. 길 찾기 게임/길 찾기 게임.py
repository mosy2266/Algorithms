import sys
sys.setrecursionlimit(10**5)

def solution(nodeinfo):
    answer = [[],[]]
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    nodeinfo.sort(key=lambda x: x[0])
    
    def traverse(tree):
        if tree:
            n,y,idx = (-1,-1,-1)
            for i in range(len(tree)):
                if tree[i][1] > y:
                    n,y,idx = tree[i][2], tree[i][1], i
            left_tree = tree[:idx]
            right_tree = tree[idx+1:]
            answer[0].append(n)
            traverse(left_tree)
            traverse(right_tree)
            answer[1].append(n)
    
    traverse(nodeinfo)
    
    return answer