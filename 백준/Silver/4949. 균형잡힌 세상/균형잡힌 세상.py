import sys
input=sys.stdin.readline

sentence=""
while True:
    parenthesis=[]
    sentence=list(input().rstrip())
    
    if sentence==["."]:
        break

    for x in sentence:
        if x=="(" or x==")" or x=="[" or x=="]":
            parenthesis.append(x)

    parenth="".join(parenthesis)

    while "()" in parenth or "[]" in parenth:
        parenth=parenth.replace("()","")
        parenth=parenth.replace("[]","")

    if not parenth:
        print("yes")
    else:
        print("no")