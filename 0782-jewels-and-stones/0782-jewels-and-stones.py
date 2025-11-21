class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for i in jewels:
            for j in stones:
                if i==j:
                    count=count+1
        return count

        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        