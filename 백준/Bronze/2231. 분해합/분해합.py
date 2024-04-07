N=int(input())
min_num=0
#각 자리를 더한 값의 최대는 항상 자릿수*9이므로
for i in range(max(0, N-len(str(N))*9), N):
    #map 함수를 이용해서 더해줌
    div_sum=i+sum(map(int,str(i)))
    if div_sum==N:
        min_num=i
        break;

print(min_num)