# d-16 jenga night
t=int(input())
for i in range (0,t):
    n,x=map(int,input().split())
    if((x%n)==0):
        print("yes")
    else:
        print("no")
