class Solution(object):
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26
        # for char in 'abcdefghijklmnopqrstuvwxyz':
        #     if char not in sentence:
        #         return False
        #     return True
        """
        :type sentence: str
        :rtype: bool
        """
        