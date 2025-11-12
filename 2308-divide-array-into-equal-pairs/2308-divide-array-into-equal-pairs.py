class Solution(object):
    def divideArray(self, nums):
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i - 1]:
                return False
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        