n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if a.count(i)==i:
        if i in b:
            continue
        b.append(i)
print(len(b))