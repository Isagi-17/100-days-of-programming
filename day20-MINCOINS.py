# d-20 min no coins
t=int(input())
for i in range (0,t):
    x=int(input())
    if((x%5)!=0):
        print(-1)
    elif((x%10)==0):
        print(x//10)
    else:
        print((x//10)+1)

