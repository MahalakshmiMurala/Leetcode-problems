class Solution(object):
    def findDisappearedNumbers(self, nums):
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:   # not visited
                result.append(i + 1)
        return result
