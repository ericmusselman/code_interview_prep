class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # use memo-ization to save compute?
        # dp
        # base case, recurrence relation
        memo = [0] * (n + 1)
        return self.count(0, n, memo)
    
    # i=current step, n=top step
    def count(self, i, n, memo):
        if i==n:
            return 1
        elif i>n:
            return 0
        elif memo[i]>0:
            return memo[i]
        memo[i] = self.count(i+1, n, memo) + self.count(i+2, n, memo)
        return memo[i]