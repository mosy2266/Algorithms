def solution(elements):
    nums_set=set()
    n = len(elements)
    
    for i in range(1, n+1):
        l=0
        r=i-1
        
        for j in range(i):
            num_sum = sum(elements[:i])
        nums_set.add(num_sum)
        
        for k in range(1,n):
            r = (r+1)%n
            num_sum = num_sum - elements[l] + elements[r]
            l = (l+1)%n
            nums_set.add(num_sum)
    
    return len(nums_set)