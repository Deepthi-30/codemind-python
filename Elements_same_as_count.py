n=int(input())
m=list(map(int,input().split()))
o=[]
p=[]
q=0
for i in m:
    if m.count(i)==i:
        q=1
        if i in p:
            continue
        p.append(i)
if q==0:
    print("-1")
else:
    print(*p)
        