class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=s[:2]
        n=len(s)
        for i in range(2,n):
            if s[i]==res[-1]==res[-2] :
                continue
            else:
                res+=s[i]
        return res

        