def solution(str1, str2):
    
    def make_set(word):
        new_set = {}
        for i in range(len(word)-1):
            element = word[i:i+2]
            if element.isalpha():
                element = element.lower()
                if element not in new_set:
                    new_set[element] = 1
                else:
                    new_set[element] += 1
        return new_set
    
    def intersection(s1, s2):
        intersect = 0
        for i in s1:
            if i in s2:
                intersect += min(s1[i], s2[i])
        return intersect
    
    def union(s1, s2):
        union = 0
        for i in s1:
            if i in s2:
                union += max(s1[i], s2[i])
            else:
                union += s1[i]
        
        for j in s2:
            if j in s1: continue
            union += s2[j]
        return union
    
    set1 = make_set(str1)
    set2 = make_set(str2)
    
    union_len = union(set1, set2)
    intersection_len = intersection(set1, set2)
    
    if union_len == 0 and intersection_len ==0 :
        return 65536
    
    answer = int((intersection_len/union_len) * 65536)
    
    return answer