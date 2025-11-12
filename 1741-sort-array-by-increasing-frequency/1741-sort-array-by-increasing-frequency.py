class Solution(object):
    def frequencySort(self, nums):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums
