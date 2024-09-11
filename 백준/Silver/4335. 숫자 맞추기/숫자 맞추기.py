minimum,maximum=0,11
while True:
    olly=int(input())
    if olly==0:
        break
    stan=input()
    
    if stan=="too high" and maximum>olly :
        maximum=olly
    elif stan=="too low" and minimum<olly :
        minimum=olly
    elif stan=="right on":
        if olly>=maximum or olly<=minimum:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        minimum,maximum=0,11