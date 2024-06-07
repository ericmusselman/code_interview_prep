class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        tally = {}
        majority = len(nums)/2
        members = set(nums)
        
        for num in nums:
            if num not in tally:
                tally[num] = 1
            else:
                tally[num] += 1
        
        for num in members:
            if tally[num] > majority:
                return num
        return -1
    