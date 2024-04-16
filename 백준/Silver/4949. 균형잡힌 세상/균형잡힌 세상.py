import sys
input=sys.stdin.readline

while True:
    sen=input().rstrip()
    if sen==".":
        break

    if sen.count("(")!=sen.count(")") or sen.count("[")!=sen.count("]"):
        print("no")
        continue

    parenth=""
    for s in sen:
        if s in "()[]":
            parenth+=s
    
    while "()" in parenth or "[]" in parenth:
        parenth=parenth.replace("()","")
        parenth=parenth.replace("[]","")
    
    if not parenth:
        print("yes")
    else:
        print("no")