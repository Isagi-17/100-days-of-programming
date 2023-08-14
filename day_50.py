class Solution:
    def leftRotate(self, arr, n, d):
        # code here
            s=d%n
            temp=[0]*s
            for i in range(0,s):
                temp[i]=arr[i]
            for k in range(s,n):
                arr[k-s]=arr[k]
            for j in range(n-s,n):
                arr[j]=temp[j-(n-s)] 
