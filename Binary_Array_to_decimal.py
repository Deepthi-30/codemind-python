n=int(input())
l=list(map(int,input().split()))
l.reverse()
sum=0
for i in range(0,len(l)):
    sum+=l[i]*2**i
print(sum)