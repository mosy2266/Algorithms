n,m=map(int, input().split())
try:
    books=list(map(int, input().split()))

    box=0
    weight=0

    for book in books:
        weight+=book
        if weight>m:
            box+=1
            weight=book
        elif weight==m:
            box+=1
            weight=0
        
    if weight>0:
        box+=1

    print(box)
except:
    print(0)