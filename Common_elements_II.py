a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
for i in c:
    if i not in d:
        if i not in e:
            e.append(i)
for i in d:
    if i not in c:
        if i not in e:
            e.append(i)
print(*e)