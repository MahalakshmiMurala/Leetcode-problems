class Solution(object):
    def finalValueAfterOperations(self, operations):
        n=len(operations)
        x=0
        for i in range(n):
            temp=operations[i]
            if temp=="X--":
                x=x-1
            if temp=="--X":
                x=x-1
            if temp=="X++":
                x=x+1
            if temp=="++X":
                x=x+1
        return x
            

        """
        :type operations: List[str]
        :rtype: int
        """
        