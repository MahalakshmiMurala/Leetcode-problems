class Solution(object):
    def mostWordsFound(self, sentences):
        ans=0
        for j in range(len(sentences)):
            s=sentences[j]
            temp=1
            for i in range(len(s)):
                ch=s[i]
                if ch==" ":
                    temp+=1
            ans=max(ans,temp)
        return ans 
        """
        :type sentences: List[str]
        :rtype: int
        """
        