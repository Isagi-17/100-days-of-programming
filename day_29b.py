class Solution:
    def printTriangle(self, N):
        sum=0
        for i in range(0,N):
            for j in range(1,i+2):
                sum=sum+1
                print(sum,end=' ')
            print()
