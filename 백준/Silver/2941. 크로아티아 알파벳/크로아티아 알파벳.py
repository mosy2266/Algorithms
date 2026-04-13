cro_al=['c=','c-','dz=','d-','lj','nj','s=','z=']
test=input()

for i in cro_al:
    test=test.replace(i,'*')

print(len(test))