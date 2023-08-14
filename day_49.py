class Solution(object):
    def rotate(self, nums, k,):
            l=len(nums)
            n=k%l
            f=nums[-n:]
            nums[n:]=nums[:-n]
            nums[:n]=f     
