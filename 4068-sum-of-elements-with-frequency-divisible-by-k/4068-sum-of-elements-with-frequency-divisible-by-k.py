class Solution(object):
    def sumDivisibleByK(self, nums, k):
        dct={}
        total=0
        for i in nums:
            if i in dct:
                dct[i]+=1
            else:
                dct[i]=1
        for key,value in dct.items():
            if(value%k==0):
             total+=key*value
        return total
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        