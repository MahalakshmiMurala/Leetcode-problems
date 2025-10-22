class Solution(object):
    def hasMatch(self, s, p):
        p=p.split('*')
        if p[0] in s:
            x=s[s.index(p[0])+len(p[0]):]
            if p[1] in x:
                return True
        return False

        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        