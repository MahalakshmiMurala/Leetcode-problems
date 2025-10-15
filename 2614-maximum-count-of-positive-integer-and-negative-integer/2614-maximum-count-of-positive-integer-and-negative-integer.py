class Solution(object):
    def maximumCount(self, nums):
        pos=0
        neg=0
        n=len(nums)
        for i in range(n):
            if nums[i]>0:
                pos+=1
            elif nums[i]<0:
                neg+=1
        return max(pos,neg)
        """
        :type nums: List[int]
        :rtype: int
        """
        