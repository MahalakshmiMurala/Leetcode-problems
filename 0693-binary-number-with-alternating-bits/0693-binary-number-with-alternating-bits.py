class Solution(object):
    def hasAlternatingBits(self, n):
        # Convert number to binary string (remove '0b' at start)
        binary = bin(n)[2:]
        
        # Check each adjacent pair of bits
        for i in range(len(binary) - 1):
            if binary[i] == binary[i + 1]:
                return False
        return True
