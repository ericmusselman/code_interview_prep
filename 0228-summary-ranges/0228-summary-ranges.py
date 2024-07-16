class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # question: negative numbers?
        i = 0
        bounds = []
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i += 1
            
            if start != nums[i]:
                bounds.append(str(start) + "->" + str(nums[i]))
            else:
                bounds.append(str(nums[i]))
                
            i += 1
        
        return bounds
    
    # Time: O(n), Space: O(1)
    