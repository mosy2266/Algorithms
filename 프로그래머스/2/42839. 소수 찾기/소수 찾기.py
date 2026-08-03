from itertools import permutations
import math

def solution(numbers):
    num_list = list(numbers)
    n = len(numbers)
    primes = set()
    
    for i in range(1, n+1):
        nums = list(permutations(num_list, i))
        for k in nums:
            num = int(''.join(k))
            if is_prime(num):
                primes.add(num)
    return len(primes)

def is_prime(num):
    if num<2: return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True