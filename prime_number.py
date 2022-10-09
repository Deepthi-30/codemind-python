def factor_count(n):
    fc=0
    for i in range(1,num+1):
        if n%i==0:
            fc+=1
    return fc
num=int(input())
fc=factor_count(num)
if fc==2:
    print("prime")
else:
    print("not a prime")