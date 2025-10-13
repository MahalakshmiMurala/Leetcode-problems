class Solution(object):
    def getRow(self, rowIndex):
        result=[]
        start=1
        result.append(start)
        for i in range(rowIndex):
            start*=(rowIndex-i)
            start//=(i+1)
            result.append(start)
        return result
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        