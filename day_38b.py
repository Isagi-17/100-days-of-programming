class Solution:
	def binary_to_decimal(self, str):
		# Code here
        s=int(str)
        a=0
        b=0
        while(s!=0):
              a=a+(s%10)*pow(2,b)
              s=s//10
              b=b+1
        return a 
