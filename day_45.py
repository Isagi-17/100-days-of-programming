class Solution:
    def sumOfDivisors(self, N):
    	#code here 
        sum=0
        for i in range(1,N+1):
            for j in range(1,i+1):
                if(i%j==0):
                     sum=sum+j
        return sum
