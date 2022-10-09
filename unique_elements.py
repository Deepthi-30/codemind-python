n=int(input())
m=list(map(int,input().split()))
o=[]
for i in m:
    if i not in o:
        o.append(i)
print(*o)