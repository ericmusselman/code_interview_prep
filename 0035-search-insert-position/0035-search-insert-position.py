class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # binary search log(n)
        lower, upper = 0, len(nums)-1
        while upper >= lower:
            mp = (lower+upper)//2
            if nums[mp] == target:
                return mp
            elif nums[mp] > target:
                upper = mp-1
            else:
                lower = mp+1
        return lower
