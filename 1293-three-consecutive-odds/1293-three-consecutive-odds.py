class Solution(object):
    def threeConsecutiveOdds(self, arr):
        n=len(arr)
        for i in range(n-2):
            if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
                return True
        return False
        """
        :type arr: List[int]
        :rtype: bool
        """
        