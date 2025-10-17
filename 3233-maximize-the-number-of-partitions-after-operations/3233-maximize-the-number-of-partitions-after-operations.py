class Solution(object):
    def maxPartitionsAfterOperations(self, s, k):
        
        N = len(s)
        if k == 26:
            return 1

        memo = {}

        def calc(index, mask, used):
            if index == N:
                return 0

            if (index, mask, used) in memo:
                return memo[(index, mask, used)]

            best = 0
            char_bit = 1 << (ord(s[index]) - ord('a'))
            new_mask = mask | char_bit

            if bin(new_mask).count('1') <= k:
                best = max(best, calc(index + 1, new_mask, used))
            else:
                best = max(best, 1 + calc(index + 1, char_bit, used))

            if not used:
                for c in range(26):
                    char_bit = 1 << c
                    new_mask = mask | char_bit
                    if bin(new_mask).count('1') <= k:
                        best = max(best, calc(index + 1, new_mask, True))
                    else:
                        best = max(best, 1 + calc(index + 1, char_bit, True))

            memo[(index, mask, used)] = best
            return best

        return calc(0, 0, False) + 1