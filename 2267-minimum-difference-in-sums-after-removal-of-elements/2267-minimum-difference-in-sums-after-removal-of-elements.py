import heapq

class Solution(object):
    def minimumDifference(self, nums):
        n = len(nums) // 3
        total_len = 3 * n

        # 1. Compute prefix min-sum for left side using max-heap
        left_heap = []
        left_sum = 0
        left_sums = [0] * total_len

        for i in range(2 * n):
            heapq.heappush(left_heap, -nums[i])  # max-heap
            left_sum += nums[i]

            if len(left_heap) > n:
                left_sum += heapq.heappop(left_heap)  # subtract max (as negative)
            
            if len(left_heap) == n:
                left_sums[i] = left_sum

        # 2. Compute suffix max-sum for right side using min-heap
        right_heap = []
        right_sum = 0
        right_sums = [0] * total_len

        for i in range(total_len - 1, n - 1, -1):
            heapq.heappush(right_heap, nums[i])  # min-heap
            right_sum += nums[i]

            if len(right_heap) > n:
                right_sum -= heapq.heappop(right_heap)  # remove smallest
            
            if len(right_heap) == n:
                right_sums[i] = right_sum

        # 3. Compute minimum difference
        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            if right_sums[i + 1]:
                diff = left_sums[i] - right_sums[i + 1]
                min_diff = min(min_diff, diff)

        return min_diff
