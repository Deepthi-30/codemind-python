a=int(input())
d=[]
flag=0;q=0;w=0
def prime(x):
    if x==1 or x==0:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
for i in range(1,a+1):
    if a%i==0:
        d.append(i)
for i in range(0,len(d)):
    for j in range(i+1,len(d)):
        if d[i]*d[j]==a:
            if prime(d[i]) and prime(d[j]):
                flag=1
                q=int(d[i])
                w=int(d[j])
if flag==1:
    print(q,w)
else:
    print("-1")