class Solution:
    def printTriangle(self, N):
        # Code here
        k=2*N-1
        low=0
        high=k-1
        v=N
        matrix=[[0 for i in range(k)]for j in range(k)]
        for i in range(N):
            for j in range(low,high+1):
                matrix[i][j]=v
            for j in range(low+1,high+1):
                matrix[j][i]=v
            for j in range(low+1,high+1):
                matrix[high][j]=v
            for j in range(low+1,high):
                matrix[j][high]=v
            low=low+1
            high=high-1
            v=v-1
        for i in range(k):
            for j in range(k):
                print(matrix[i][j],end=' ')
            print() 
