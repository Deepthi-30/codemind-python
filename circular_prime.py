import math
a=int(input())
lis=str(a)
st=lis[::-1]
intt=int(st)
def isprime(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True
c=0
if isprime(a):
    c+=1
if isprime(intt):
    c+=1
if c==2:
    print("circular prime")
elif c==1:
    print("prime but not a circular prime")
else:
    print("not prime")