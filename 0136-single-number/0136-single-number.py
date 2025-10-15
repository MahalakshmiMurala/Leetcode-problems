class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i)==1:
                return i
                break
        # c=nums[0]
        # for i in range(1,len(nums)):
        #     c^=nums[i]
        # return c               

        