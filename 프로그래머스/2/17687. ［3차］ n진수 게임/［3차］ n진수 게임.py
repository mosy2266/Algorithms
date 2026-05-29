def solution(n, t, m, p):
    answer = ''
    
    
    cnt=1
    numbers='0'

    for _ in range(t*m):
        converted=''
        num=cnt
        while num!=0:
            match(num%n):
                case 10:
                    converted+='A'
                case 11:
                    converted+='B'
                case 12:
                    converted+='C'
                case 13:
                    converted+='D'
                case 14:
                    converted+='E'
                case 15:
                    converted+='F'
                case _:
                    converted+=str(num%n)
            num=num//n
        converted=converted[-1::-1]
        numbers+=converted
        cnt+=1
    
    for i in range(t):
        answer+=numbers[(p+i*m)-1]
    
    return answer