a,b,c=map(int,input().split())
sum=0
cnt=0
for i in range(a,b+1):
    if i%c==0:
        cnt+=1
        sum+=i
print(cnt)