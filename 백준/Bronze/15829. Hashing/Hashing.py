L=int(input())
strings=input()

answer=0
for i in range(len(strings)):
    answer+=((ord(strings[i])-96)*(31**i))
    answer%=1234567891
print(answer)