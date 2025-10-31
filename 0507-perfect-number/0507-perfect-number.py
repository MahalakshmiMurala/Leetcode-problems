class Solution(object):
    def checkPerfectNumber(self, num):
        if num==1:
            return False
        sm=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                sm+=i
                if i!=num//i:
                    sm+=num//i
                # print(sm)
        return sm==num

        # if num<=1:
        #     return False
        # s=0
        # for i in range(1,num):
        #     if num%i==0:
        #         s=s+i
        # return s==num

        """
        :type num: int
        :rtype: bool
        """
        