a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
e=[]
for i in range(a):
    if c>b[i] or d<b[i]:
        e.append(b[i])
print(sum(e))