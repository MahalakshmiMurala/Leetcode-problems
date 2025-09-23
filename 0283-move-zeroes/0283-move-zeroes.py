class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Pointer for placing the next non-zero
        last_non_zero = 0  

        # Step 1: Move all non-zeros forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1

        # Step 2: Fill remaining with zeros
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0
