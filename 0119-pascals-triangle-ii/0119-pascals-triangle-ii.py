class Solution(object):
    def getRow(self, rowIndex):
        r=[]
        s=1
        r.append(s)
        for i in range(rowIndex):
            s*=(rowIndex-i)
            s//=(i+1)
            r.append(s)
        return r
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        