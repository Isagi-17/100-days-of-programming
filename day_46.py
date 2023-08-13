class Solution:
        def print2largest(self,arr, n):
		# code here
		s=set(arr)
		l=len(s)
		if(l>1):
		     a=list(s)
             a.sort()
             return a[-2]
        else:
            return -1
               
                
