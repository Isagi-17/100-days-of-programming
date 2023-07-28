# d-21 gross salary
t=int(input())
for i in range (0,t):
    s=int(input())
    if(s<1500):
        print(s+s)
    else:
        print(s+500+(s*0.98))
