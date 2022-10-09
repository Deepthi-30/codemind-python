n=int(input())
m=list(map(int,input().split()))
o=[]
p=[]
for i in range(len(m)):
    if m[i]%2==1 and i%2==1:
        o.append(i)
for j in m:
    if j%2==1:
        p.append(j)
if len(p)==len(o):
    print("True")
else:
    print("False")