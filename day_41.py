class Solution:
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        temp=0
        for i in range(1,n):
             for j in range(i,0,-1):
                 if(alist[j]<alist[j-1]):
                     temp=alist[j]
                     alist[j]=alist[j-1]
                     alist[j-1]=temp
                 else:
                     break
