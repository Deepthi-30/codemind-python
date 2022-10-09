a=int(input())
m=list(map(int,input().split()))
c,d=map(int,input().split())
o=[]
p=0
for i in range(a):
    if c>m[i] or d<m[i]:
        o.append(m[i])
        p=1
if p==0:
    print("-1")
else:
    print(max(o))