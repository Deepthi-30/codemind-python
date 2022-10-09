a,d=map(int,input().split())
b=list(map(int,input().split()))
count=0
for i in range(0,len(b)):
    c=str(abs(b[i]))
    if len(c)==d:
        count+=1
print(count)
    