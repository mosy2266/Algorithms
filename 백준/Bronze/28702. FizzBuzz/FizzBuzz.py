def fizzbuzz(i):
    if i%3==0 and i%5==0:
        return "FizzBuzz"
    elif i%3==0 and i%5!=0:
        return "Fizz"
    elif i%3!=0 and i%5==0:
        return "Buzz"
    else:
        return i

fb=[]
for _ in range(3):
    fb.append(input())

if fb[2].isdigit()==True:
    print(fizzbuzz(int(fb[2])+1))
    
elif fb[1].isdigit()==True:
    print(fizzbuzz(int(fb[1])+2))

elif fb[0].isdigit()==True:
    print(fizzbuzz(int(fb[0])+3))