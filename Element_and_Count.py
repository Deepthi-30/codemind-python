a=int(input())
b=list(map(int,input().split()))
c=[]
e=[]
for i in b:
    if i in c:
        continue
    c.append(i)
for j in c:
    e.append(j)
    e.append(b.count(j))
print(*e)