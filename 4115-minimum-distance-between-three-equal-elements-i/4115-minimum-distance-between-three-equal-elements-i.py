class Solution(object):
    def minimumDistance(self, nums):
        n = len(nums)
        min_dist = float('inf')  
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        dist = abs(i - j) + abs(j - k) + abs(k - i)
                        min_dist = min(min_dist, dist)
        return min_dist if min_dist != float('inf') else -1
