class Solution:
    def countLargestGroup(self, n):
        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        groups = {} 

        for num in range(1, n + 1):
            s = digit_sum(num)
            if s in groups:
                groups[s] += 1
            else:
                groups[s] = 1

        max_size = 0
        count = 0

        for size in groups.values():
            if size > max_size:
                max_size = size
                count = 1
            elif size == max_size:
                count += 1

        return count
