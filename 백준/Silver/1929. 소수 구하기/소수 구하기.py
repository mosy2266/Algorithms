M,N=map(int, input().split())

def primenums(M,N):
    primes=set(range(M,N+1))
    if 1 in primes:
        primes.remove(1)
    for i in range(2, int(N**0.5)+1):
        primes-=set(range(i*2, N+1, i))
    return list(primes)

nums=sorted(primenums(M,N))

for num in nums:
    print(num)