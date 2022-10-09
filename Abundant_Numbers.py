N=int(input())
factorsum=0
for i in range(1,N):
    if N%i==0:
        factorsum+=i
if factorsum>N:
    print("True")
else:
    print("False")