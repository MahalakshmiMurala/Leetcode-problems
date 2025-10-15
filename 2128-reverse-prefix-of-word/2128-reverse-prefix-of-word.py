class Solution:
    def reversePrefix(self, word,ch):
        idx=word.find(ch)    
        if idx:
            return word[:idx+1][::-1]+ word[idx+1:]
        return word
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        