class Solution:
    def printTriangle(self, N):
        for i in range(0,N):
            for j in range(0,i+1):
                print('*',end=' ')
            print()    
        for k in range(N-1,0,-1):
            for h in range(0,k):
                print('*',end=' ')
            print()
