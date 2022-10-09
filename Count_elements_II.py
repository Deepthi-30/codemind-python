a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
f=[]
for i in c:
    if i not in d:
        if i not in e:
            e.append(i)
for j in d:
    if j not in c:
        if j not in f:
            f.append(j)
print(len(e)+len(f))