a=int(input())
b=i=list(map(int,input().split()))
d=[]
for i in range(0,len(b)):
    if b[i]%2==0:
        break
for j in range(len(b)-1,-1,-1):
    if b[j]%2==0:
        break
c=b[i+1:j]
for k in c:
    if k%2==0:
        d.append(k)
print(len(d))