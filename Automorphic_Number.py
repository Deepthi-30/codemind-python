n=int(input())
a=n*n
while n:
    if a<100:
        b=a%10
    if a>100 and a<10000:
        b=a%100
    if a>10000:
        b=a%1000
    if n==b:
        print("Automorphic Number")
        break
    else:
        print("Not an Automorphic Number")
        break