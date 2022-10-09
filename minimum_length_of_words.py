a=list(map(str,input().split()))
b=[]
for c in a:
    b.append(len(c))
print(min(b))