a=int(input())
a=str(a)
a=list(a)
b=[]
for i in a:
    if a.count(i)<=1:
        b.append(i)
if len(b)==len(a):
    print("Unique Number")
else:
    print("Not Unique Number")