a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in b:
    if i not in c:
        c.append(i)
for i in c:
    if i%2==0:
        d.append(i)
print(sum(d))
        