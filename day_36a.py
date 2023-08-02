class Solution:
    def factorial (self, N):
        # code here
        s=1
        for i in range(1,N+1):
            s=s*i
        return s   
