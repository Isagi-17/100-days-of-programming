# d-15 minimum cars required
t=int(input())
for i in range (0,t):
    n=int(input())
    if(0<n<4):
        print(1)
    elif((n%4)==0):
        print(n//4)
    else:
        print((n//4)+1)
