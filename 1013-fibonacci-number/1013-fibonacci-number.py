class Solution(object):
    def fib(self, n):
        # f(0)=0
        # f(1)=1
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)
      
        