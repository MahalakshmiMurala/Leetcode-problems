class Solution(object):
    def isMonotonic(self, nums):
        n = len(nums)
        inc = True
        dec = True

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dec = False
            elif nums[i] < nums[i - 1]:
                inc = False

        return inc or dec
        """
        :type nums: List[int]
        :rtype: bool
        """
        