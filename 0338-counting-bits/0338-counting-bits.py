class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)  # Initialize result array
        
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # DP relation
            
        return ans
