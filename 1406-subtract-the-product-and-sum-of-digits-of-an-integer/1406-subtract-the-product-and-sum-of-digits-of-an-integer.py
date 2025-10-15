class Solution(object):
    def subtractProductAndSum(self, n):
        prod=1
        sum1=0
        while n>0:
            d=n%10
            prod=prod*d
            sum1=sum1+d
            n=n//10
            res=prod-sum1
        return res 


        """
        :type n: int
        :rtype: int
        """
        