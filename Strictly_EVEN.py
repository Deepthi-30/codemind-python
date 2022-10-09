n=int(input())
m=list(map(int,input().split()))
o=[]
p=[]
for i in range(len(m)):
    if i%2==0 and m[i]%2==0:
        o.append(i)
for j in m:
    if j%2==0:
        p.append(i)
if len(o)==len(p):
    print("True")
else:
    print("False")