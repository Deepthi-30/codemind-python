a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
co=0
for i in set(c):
    if i in set(d):
        co+=1
print(co)