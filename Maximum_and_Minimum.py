j=int(input())
k=list(map(int,input().split()))
l=[]
m=0
for j in k:
    if k.count(j)==j:
        m=1
        if j in l:
            continue
        l.append(j)
if m==0:
    print("-1")
else:
    print(min(l),max(l))