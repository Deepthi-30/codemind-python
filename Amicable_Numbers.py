a=int(input())
b=int(input())
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i
sum1=0
for i in range(1,b):
    if b%i==0:
        sum1+=i
if sum==b and sum1==a:
    print("Amicable")
else:
    print("Not Amicable")
