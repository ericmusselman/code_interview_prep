class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            test = target - nums[i]
            if test in map:
                return [i, map[test]]
            map[nums[i]] = i
        