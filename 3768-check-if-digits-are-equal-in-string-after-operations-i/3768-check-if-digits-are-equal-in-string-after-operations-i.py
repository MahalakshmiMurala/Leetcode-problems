class Solution(object):
    def hasSameDigits(self, s):
        s = list(map(int, str(s)))
        dump = []

        for i in range(len(s)):
            for j in range(1, len(s)):
                dev = (s[j-1]+s[j])%10
                dump.append(dev)
            if len(dump) == 2:
                if dump[0] == dump[1]:
                    return True
            s = []
            s = dump
            dump = []
        return False