class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = [words[0]]
        
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])
                
        return result
