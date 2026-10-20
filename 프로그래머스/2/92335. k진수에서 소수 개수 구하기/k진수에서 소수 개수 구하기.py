def solution(n, k):
    answer = 0
    
    def convert_to_n(num, base):
        result = []
        
        while num>0:
            num, remainder = divmod(num, base)
            result.append(str(remainder))
        
        return ''.join(reversed(result))
    
    def is_prime(num):
        if num == 1: return False
        
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
    
    numbers = list(convert_to_n(n,k).split('0'))

    for number in numbers:
        if number.isdecimal():
            if is_prime(int(number)):
                answer+=1
    
    return answer