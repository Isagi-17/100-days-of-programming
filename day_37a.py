#factorial using recursion
def fact(n):
        if(n==1):
            return 1
        return n*fact(n-1)
n=int(input("enter the value"))
if(n<1):
    print("factorial does not exist")
else:    
    print(fact(n))
