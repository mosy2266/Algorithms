N,K=map(int, input().split())
a=b=1
#분자의 경우 N!/(N-K)! = (N * N-1 * ... * N-K+1)가 되므로
for i in range(N, N-K, -1):
    a*=i
#분모의 경우 K!만 남으므로
for i in range(1,K+1):
    b*=i
#정수형으로 출력해야 함
print(int(a/b))