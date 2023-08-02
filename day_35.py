class Solution:
    def reverse(self, x: int) -> int:
        max=pow(2,31)-1
        max=int(max)
        min=pow(-2,31)
        min=int(min)
        a=x
        if x<0:
            x=x*(-1)
        s=0
        while(x>0):
            s=s*10+x%10
            x=x//10
        if s not in range(min,max):
            return 0
        elif(a<0):
            return s*(-1)
        else:
            return s  
