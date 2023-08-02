class Solution:
    def isPrime (self, N):
        # code here
        c=0
        if(N==1):
            return 0
        else:
            for i in range(2,N):
                if(N%i==0):
                    c=1
                    break
        if(c==1):
            return 0
        else:
            return 1
