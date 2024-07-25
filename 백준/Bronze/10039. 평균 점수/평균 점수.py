all=0
for _ in range(5):
    score=int(input())
    if score<40:
        all+=40
        continue
    all+=score
print(all//5)