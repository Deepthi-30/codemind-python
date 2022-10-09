a=int(input())
c=0
def isprime(x):
    if x==1 or x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
for i in str(a):
    if isprime(int(i)):
        c+=1
if c==len(str(a)) and isprime(a)==True:
    print("Mega Prime")
else:
    print("Not Mega Prime")