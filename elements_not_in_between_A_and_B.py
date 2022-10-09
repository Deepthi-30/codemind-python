n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
k=0
d=[]
for i in range(n):
    if a>m[i] or b<m[i]:
        d.append(m[i])
        k=1
if k==0:
    print("-1")
else:
    print(*d)