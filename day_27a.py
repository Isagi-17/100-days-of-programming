class Solution:
    def printTriangle(self, N):
        s=N-1
        for i in range(0,N):
            for j in range(0,s):
                print (end=' ')
            s=s-1
            for K in range(0,2*i+1):
                print('*',end='')
            print() 
