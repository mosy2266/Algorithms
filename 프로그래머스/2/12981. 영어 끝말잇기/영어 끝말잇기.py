def solution(n, words):
    answer = []
    num=0
    order=1
    used_words=set()
    
    prev_word=words[0]
    used_words.add(words[0])
    for i in range(1, len(words)):
        num=(i+1)%n
        if num==0:
            num=n
        if i%n==0:
            order+=1
        
        if prev_word[-1]!=words[i][0] or words[i] in used_words:
            return [num,order]
        
        prev_word=words[i]
        used_words.add(words[i])
    
    return [0,0]