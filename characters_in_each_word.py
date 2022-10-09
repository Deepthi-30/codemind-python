list1=list(map(str,input().split()))
list2=[]
for a in list1:
    list2.append(len(a))
print(*(list2))