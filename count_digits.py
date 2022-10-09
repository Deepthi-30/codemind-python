a=int(input())
b=list(map(int,input().split()))
for i in range(len(b)):
    a=str(abs(b[i]))
    print(len(a),end=" ")