n=int(input())#123
m=abs(n)
rev=0
while m>0:
    d=m%10
    rev=rev*10+d
    m=m//10
if n<0:
    print(-rev)
else:
    print(rev)