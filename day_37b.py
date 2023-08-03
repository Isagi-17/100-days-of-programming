#fibonacci series using recursion
def fib(n):
    if(n<=1):
        return n
    return fib(n-1)+fib(n-2)
n=int(input("enter the value"))
print(fib(n))
