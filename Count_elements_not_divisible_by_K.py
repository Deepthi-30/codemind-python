a,b=map(int,input().split())
c=list(map(int,input().split()))
d=[]
for i in c:
    if i%b!=0:
        d.append(i)
print(len(d))