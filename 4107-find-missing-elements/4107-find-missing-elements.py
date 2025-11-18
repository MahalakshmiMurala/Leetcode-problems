class Solution(object):
    def findMissingElements(self, nums):
        x=[]
        for i in range(min(nums),max(nums)):
            if i not in nums:
                x.append(i)
        return x
                
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        