n=int(input())
m=list(map(int,input().split()))
o=[]
p=[]
for i in m:
    if i not in o:
        o.append(i)
for i in o:
    if i%2==1:
        p.append(i)
print(sum(p))