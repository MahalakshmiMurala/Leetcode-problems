class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1) - 1, len(num2) - 1  # pointers starting from rightmost digit
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            # Get current digits or 0 if index is out of range
            x = ord(num1[i]) - ord('0') if i >= 0 else 0
            y = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = x + y + carry
            result.append(str(total % 10))  # store the current digit
            carry = total // 10  # update carry

            i -= 1
            j -= 1

        # Since we added from least significant digit, reverse at the end
        return ''.join(result[::-1])
