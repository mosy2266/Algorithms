N=int(input())

beehive=1
distance=1
while N>beehive:
    beehive+=(6*distance)
    distance+=1
print(distance)