num=int(input())
while num:
    a=num//1000
    b=num%1000
    c=b//100
    d=b%100
    e=d//10
    f=d%10
    g=max(a,c,e,f)
    print(g)
    break