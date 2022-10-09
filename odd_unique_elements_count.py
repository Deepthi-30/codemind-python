n=int(input())
m=list(map(int,input().split()))
o=[]
c=0
for i in m:
    if i not in o:
        o.append(i)
for i in o:
    if i%2==1:
        c+=1
print(c)