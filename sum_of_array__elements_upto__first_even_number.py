n=int(input())
m=list(map(int,input().split()))
o=[]
for i in m:
    if i%2==1:
        o.append(i)
    if i%2==0:
        break
print(sum(o))