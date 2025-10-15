class Solution(object):
    def countDigits(self, num):
        temp=num
        count=0
        while temp>0:
            d=temp%10
            if d!=0 and num%d==0:
                count+=1
            temp=temp//10
        return count
        """
        :type num: int
        :rtype: int
        """
        