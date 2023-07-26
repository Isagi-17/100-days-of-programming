# d-12sata shark tank
t=int(input())
for i in range (0,t):
    a,b=map(int,input().split())
    if((a*10)==(b*5)):
        print("ANY")
    elif((a*10)>(b*5)):    
        print("FIRST")
    else:
        print("SECOND")
