n=int(input())
m=list(map(int,input().split()))
o=[]
for i in range(len(m)):
    if m[i]==0 or m[i]==1:
        o.append(m[i])
if len(m)==len(o):
    print("True")
else:
    print("False")