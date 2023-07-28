#d-22 deg of polynomial
t=int(input())
for i in range (0,t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    for i in range(0,n):
        if(a[n-1]!=0):
            print(n-1)
            break
        else:
            n=n-1
            