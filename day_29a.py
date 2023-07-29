class Solution:
    def printTriangle(self, N):
        s=2*(N-1)
        for i in range(0,N):
            for j in range(1,i+2):
                print(j,end=' ')
            for k in range(0,s):
                print(end='  ')
            s=s-2
            for h in range(i+1,0,-1):
                print(h,end=' ')
            print()    
