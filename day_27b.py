class Solution:
    def printTriangle(self, N):
        s=0
        for i in range(N,0,-1):
            for j in range(0,s):
                print (end=' ')
            s=s+1
            for K in range(0,2*i-1):
                print('*',end='')
            print()  
