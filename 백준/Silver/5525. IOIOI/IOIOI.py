#실패 함수(전처리 함수)
def KMP_table(pattern):
    pat_lng=len(pattern)
    table=[0 for _ in range(pat_lng)]

    pref=0
    for suff in range(1, pat_lng):
        while pref>0 and pattern[pref]!=pattern[suff]:
            pref=table[pref-1]
        
        if pattern[pref]==pattern[suff]:
            pref+=1
            table[suff]=pref

    return table

#KMP 알고리즘
def KMP_algorithm(string, pattern):
    table=KMP_table(pattern)
    result=0
    pref=0
    for idx in range(len(string)):
        while pref>0 and string[idx]!=pattern[pref]:
            pref=table[pref-1]
        
        if string[idx]==pattern[pref]:
            pref+=1
            if pref == len(pattern):
                result+=1
                pref=table[pref-1]
    return result

n=int(input())
m=int(input())
s=input()

p_n=[]
for i in range(1, 2*n+2):
    if i%2!=0:
        p_n.append('I')
    else:
        p_n.append('O')
p_n=''.join(p_n)

print(KMP_algorithm(s,p_n))