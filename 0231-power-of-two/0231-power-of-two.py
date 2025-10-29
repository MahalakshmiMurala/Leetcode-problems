class Solution(object):
    def isPowerOfTwo(self, n):
        if n%2==0 or n==1:
            return True
        else:
            return False
        # for x in range(31):
        #     if n==2**x:
        #         return True
        # return False
        """
        :type n: int
        :rtype: bool
        """
        