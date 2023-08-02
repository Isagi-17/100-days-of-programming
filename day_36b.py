class Solution:
    def fib(self, n: int) -> int:
        f0=0
        f1=1
        a=0
        if(n==0):
            return 0
        elif(n==1):
            return 1
        else:
            for i in range(1,n):
                a=f0+f1
                f0=f1
                f1=a
            return a            
