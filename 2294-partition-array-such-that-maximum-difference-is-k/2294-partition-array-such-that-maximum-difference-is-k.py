class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        output = 1
        left = nums[0]
        
        for i in range(len(nums)):
            if nums[i] - left > k:
                left = nums[i]
                output += 1
        return output
                