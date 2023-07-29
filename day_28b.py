class Solution:
    def printTriangle(self, N):
        for i in range(0,N):
            for j in range(i+1,0,-1):
                if(j%2!=0):
                    print(1,end=' ')
                else:
                    print(0,end=' ')
            print()
