class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        count = 0
        for i in nums:
            if i %  2 == 0:
                count |= i
        return count        