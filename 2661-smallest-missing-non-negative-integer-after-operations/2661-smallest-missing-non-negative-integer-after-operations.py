from collections import Counter

class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        # Count frequency of remainders modulo value
        rem_count = Counter(num % value for num in nums)
        
        mex = 0
        while True:
            r = mex % value
            if rem_count[r] > 0:
                rem_count[r] -= 1
                mex += 1
            else:
                # No more numbers with this remainder
                return mex
