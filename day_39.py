class Solution: 
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(0,n):
            smallest=arr[i]
            sm_index=i
            for j in range(i+1,n):
                if(arr[j]<smallest):
                    smallest=arr[j]
                    sm_index=j
            arr[i],arr[sm_index]=arr[sm_index],arr[i]
