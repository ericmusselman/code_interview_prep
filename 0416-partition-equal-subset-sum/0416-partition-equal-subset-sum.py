class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # top down dp with memoization
        @lru_cache(maxsize=None)
        def dfs(nums, n, subset_sum):
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            
            output = (dfs(nums, n-1, subset_sum-nums[n-1]) or dfs(nums, n-1, subset_sum))
            return output
        
        total = sum(nums)
        if total%2 != 0:
            return False
        
        subset_sum = total//2
        n = len(nums)
        
        # pass in index, remove (and optionally not) until subset_sum negative, return True if == 0
        return dfs(tuple(nums), n-1, subset_sum)