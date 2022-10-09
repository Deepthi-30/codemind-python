j=int(input())
k=list(map(int,input().split()))
l=0
m=[]
for i in k:
    if k.count(i)==i:
        l=1
        if i in m:
            continue
        m.append(i)
if l==0:
    print("-1")
else:
    avg=(sum(m)/len(m))
    e='%.2f'%avg
    print(e)