class Solution(object):
    def bitwiseComplement(self, n):
        a=bin(n)[2:]
        b=''
        for bit in a:
            if bit=='0':
                b+='1'
            else:
                b+='0'
        return int(b,2)
        """
        :type n: int
        :rtype: int
        """
        