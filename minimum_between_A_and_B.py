n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
o=[]
s=0
for i in m:
    if a<=i<=b:
        o.append(i)
        s=1
if s==0:
    print(-1)
else:
    print(min(o))