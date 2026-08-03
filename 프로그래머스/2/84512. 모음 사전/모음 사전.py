from itertools import product

def solution(word):
    answer = 0

    vowels = ['A','E','I','O','U']
    words = []
    
    for i in range(1, 6):
        vowel_prod = list(product(vowels, repeat=i))
        for j in vowel_prod:
            words.append(''.join(j))
    
    words.sort()
    
    for w in words:
        answer+=1
        if w == word:
            break
    
    return answer