class Solution(object):
    def minimumOperations(self, nums):
        n = len(nums)
        
        ops = 0
        while 3 * ops <= n:
            remaining = nums[3 * ops :]
            if len(remaining) == len(set(remaining)):
                return ops
            ops += 1
        
        return ops
