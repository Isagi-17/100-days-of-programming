class Solution(object):
    def check(self, nums):
         sort_list=sorted(nums)
         for i in range(len(nums)):
             if(nums[i:]+nums[:i]==sort_list):
                 return True
         return False    
