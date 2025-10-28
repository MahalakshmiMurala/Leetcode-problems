class Solution(object):
    def reverseWords(self, s):
        l=[]
        s=s.split()
        for i in s:
            l.append(i[::-1])
        return " ".join(l)
        """
        :type s: str
        :rtype: str
        """
        