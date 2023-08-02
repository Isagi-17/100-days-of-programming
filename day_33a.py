class Solution:
    def armstrongNumber (self, n):
        # code here 
        k=n%10
        a=n//10
        l=a%10
        b=a//10
        c=(k*k*k)+(l*l*l)+(b*b*b)
        if(n!=c):
           return 'No'
        else:
            return 'Yes'
        
