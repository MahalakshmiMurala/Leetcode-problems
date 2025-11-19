class Solution(object):
    def isOneBitCharacter(self, bits):
        n = len(bits)
        i = 0
        while i < n - 1:
            i += bits[i] + 1
        return i == n - 1
        """
        :type bits: List[int]
        :rtype: bool
        """
        