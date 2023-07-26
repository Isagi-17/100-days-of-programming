# d-14 qualify round
t=int(input())
for i in range(0,t):
    x,a,b=map(int,input().split())
    if(x<=(a+(b*2))):
        print("qualify")
    else:
        print("notqualify")
