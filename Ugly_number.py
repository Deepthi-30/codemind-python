def isugly(n):
    if(n==1):
        return 1
    if(n<=0):
        return 0
    if(n%2==0):
        return(isugly(n//2))
    if(n%3==0):
        return(isugly(n//3))
    return 0
n=int(input())
no=isugly(n)
if(no==1):
    print("Ugly Number")
else:
    print("Not Ugly Number")
