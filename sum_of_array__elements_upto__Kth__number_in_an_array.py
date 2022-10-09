n=int(input())
m=list(map(int,input().split()))
o=int(input())
p=[]
for i in range(o):
    p.append(m[i])
print(sum(p))