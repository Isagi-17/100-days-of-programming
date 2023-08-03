class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        temp=0
        for i in range(0,n-1):
            for j in range(0,n-i-1):
                if(arr[j]>arr[j+1]):
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
