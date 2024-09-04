import sys
input=sys.stdin.readline

n=int(input())
books=dict()

for _ in range(n):
    title=input().rstrip()
    if title not in books:
        books[title]=1
    else:
        books[title]+=1

solded=sorted(books.items(), key=lambda x: (-x[1], x[0]))

print(solded[0][0])