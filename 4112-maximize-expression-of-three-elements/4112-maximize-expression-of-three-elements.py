class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        nums.sort()
        res=nums[-1]+nums[-2]-nums[0]
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        