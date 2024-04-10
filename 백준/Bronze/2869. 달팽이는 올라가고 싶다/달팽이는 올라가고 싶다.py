A,B,V=map(int, input().split())

if (V-B)%(A-B)==0:
    print((V-B)//(A-B))
else:
   print((V-B)//(A-B)+1)