class Solution(object):
    def singleNumber(self, nums):
        c=nums[0]
        for i in range(1,len(nums)):
            c^=nums[i]
        return c               

        