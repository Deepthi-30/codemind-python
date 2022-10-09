a=int(input())
b=list(map(int,input().split()))
c=sorted(b)
c.reverse()
if c==b:
    print("yes")
else:
    print("no")