class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l = []
        n=len(nums)
        for i in range(0, n):
            cont = 0
            for j in range(0,n):
                if i == j:
                    continue
                if nums[j] < nums[i]:
                    cont += 1
            l.append(cont)
        return l
                
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        