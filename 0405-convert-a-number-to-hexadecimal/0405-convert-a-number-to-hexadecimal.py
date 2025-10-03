class Solution(object):
    def toHex(self, num):
        num &= 0xFFFFFFFF; return hex(num)[2:]
