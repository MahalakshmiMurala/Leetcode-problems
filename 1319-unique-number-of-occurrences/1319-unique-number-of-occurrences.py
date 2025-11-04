class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        freq = {}
        for value in arr:
            if value in freq:
                freq[value] +=1
            else:
                freq[value] = 1
        n_occurrences = list(freq.values())
        return len(n_occurrences) == len(set(n_occurrences))

            

            

            
        