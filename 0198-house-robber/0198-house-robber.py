class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i in memo:
                return memo[i]
            
            # Recurrence relation
            memo[i] = max(dp(i-1), dp(i-2)+nums[i])
            return memo[i]
        
        memo = {}
        return dp(len(nums)-1)
    