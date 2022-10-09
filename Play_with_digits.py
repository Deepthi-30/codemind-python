b=int(input())
m=list(map(int,input().split()))
s=[str(i)for i in m]
al=int("".join(s))
o=0
while al:
    rem=al%10
    o+=rem
    al=al//10
print(o)