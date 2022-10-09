a=int(input())
sqrl=a*a
c=0
d=0
e=0
while a:
    rem=a%10
    c=c*10+rem
    a//=10
sqr2=c*c
while sqr2:
    rem=sqr2%10
    d=d*10+rem
    sqr2=sqr2//10
if sqrl==d:
    print("True")
else:
    print("False")