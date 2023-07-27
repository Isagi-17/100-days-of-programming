# d-19 find shoes
t=int(input())
for i in range(0,t):
    n,m=map(int,input().split())
    if(n>m):
        print(n+(n-m))
    else:
        print(n)
    
    
    
