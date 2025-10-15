class Solution(object):
    def isPalindrome(self,x):
        rev=0
        temp=x
        # if x<0:
        #     return False
        while x>0: 
            rem=x%10
            rev=rev*10+rem
            x=x//10
        if temp==rev:
            return True
        else:
            return False
        return #str(x)==str(x)[::-1]
        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False

        # reversed_half = 0
        # while x > reversed_half:
        #     reversed_half = reversed_half * 10 + x % 10
        #     x //= 10

        # return x == reversed_half or x == reversed_half // 10
