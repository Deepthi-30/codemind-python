n=int(input())
m=list(map(int,input().split()))
avg=sum(m)//len(m)
o=[]
for i in m:
    if i>=avg:
        o.append(i)
print(len(o))