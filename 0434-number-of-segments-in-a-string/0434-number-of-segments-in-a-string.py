class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        in_segment = False

        for char in s:
            if char != ' ' and not in_segment:
                # Starting a new segment
                count += 1
                in_segment = True
            elif char == ' ':
                # End of current segment
                in_segment = False

        return count
