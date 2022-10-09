a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in b:
    if i%2==1:
        c.append(i)
    else:
        d.append(i)
print(*(c+d))