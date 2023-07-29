class Solution:
    def printTriangle(self, N):
        s=65
        for i in range(1,N+1):
            for j in range(s,i+s):
                print(chr(j),end='')
            print()
