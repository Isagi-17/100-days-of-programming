class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if(low<high):
            pIndex=self.partition(arr,low,high)
            self.quickSort(arr,low,pIndex-1)
            self.quickSort(arr,pIndex+1,high)
        
    def partition(self,arr,low,high):
            # code here
            pivot=arr[low]
            i=low
            j=high
            while(i<j):
                 while(arr[i]<=pivot and i<=high-1):
                     i=i+1
                 while(arr[j]>=pivot and j>=low+1):
                     j=j-1
                 if(i<j):
                      arr[i],arr[j]=arr[j],arr[i]
            arr[low],arr[j]=arr[j],arr[low]
            return j
