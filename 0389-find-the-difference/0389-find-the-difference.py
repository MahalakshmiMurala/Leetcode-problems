class Solution:
    def findTheDifference(self, s, t):
        if len(s)>len(t):
            for i in s:
                if s.count(i)>t.count(i):
                    return i
                    break
        if len(t)>len(s):
            for i in t:
                if t.count(i)>s.count(i):
                    return i
                    break
        # s_sum = sum(ord(x) for x in s)
        # t_sum = sum(ord(y) for y in t)
    
        # return chr(t_sum - s_sum)