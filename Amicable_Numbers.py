a=int(input())
b=int(input())
sum1=0
sum2=0
for i in range(1,a+1):
    if a%i==0:
        sum1+=i
for i in range(1,b+1):
    if b%i==0:
        sum2+=i
if sum1==sum2:
    print("Amicable")
else:
    print("Not Amicable")