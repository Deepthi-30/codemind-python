N=int(input())
Reverse=0
flag=0
while N:
    Reminder=N%10
    Reverse=(Reverse*10)+Reminder
    N=N//10
    if N==Reverse:
        flag=1
        break
if flag==1:
    print("True")
else:
    print("False")