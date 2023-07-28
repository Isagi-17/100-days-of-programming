# d-23 second max
t=int(input())
for i in range(0,t):
    x,y,z=map(int,input().split())
    if(x>y):
        if(z>x):
            print(x)
        elif(y>z):
            print(y)
        else:
            print(z)
    elif(y>x):
        if(z>y):
            print(y)
        elif(x>z):
            print(x)
        else:
            print(z)
        
