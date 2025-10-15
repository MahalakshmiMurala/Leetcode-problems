class Solution(object):
    def interpret(self, command):
        s=command.replace("()","o")
        s=s.replace("(al)","al")
        return s
        """
        :type command: str
        :rtype: str
        """
        