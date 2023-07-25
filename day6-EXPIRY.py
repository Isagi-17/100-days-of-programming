# Expiring bread
t=int(input())
for i in range (0,t):
    n,m,k=map(int,input().split())
    if(n<=(m*k)):
        print("yes")
    else:
        print("no")
        