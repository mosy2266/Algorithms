a,b,c=map(int, input().split())

if a+b==c:
    print(a,'+',b,'=',c,sep='')
elif a-b==c:
    print(a,'-',b,'=',c,sep='')
elif a*b==c:
    print(a,'*',b,'=',c,sep='')
elif int(a/b)==c:
    print(a,'/',b,'=',c,sep='')
elif a==b+c:
    print(a,'=',b,'+',c,sep='')
elif a==b-c:
    print(a,'=',b,'-',c,sep='')
elif a==b*c:
    print(a,'=',b,'*',c,sep='')
elif a==int(b/c):
    print(a,'=',b,'/',c,sep='')